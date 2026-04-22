"""Shared test fixtures for cloudpss_skills_v2 integration tests."""

import json
import os
from pathlib import Path

import pytest


# ============================================================================
# Environment Fixtures
# ============================================================================


@pytest.fixture(scope="session")
def cloudpss_token():
    """Get CloudPSS token from env or file."""
    token = os.environ.get("CLOUDPSS_TOKEN")
    if token:
        return token

    for token_file in [".cloudpss_token", ".cloudpss_token_internal"]:
        p = Path(token_file)
        if p.exists():
            return p.read_text().strip()
    return None


@pytest.fixture(scope="session")
def cloudpss_api_url():
    """Get CloudPSS API URL."""
    return os.environ.get("CLOUDPSS_API_URL", "https://internal.cloudpss.com")


@pytest.fixture(scope="session")
def cloudpss_model_rid():
    """Get CloudPSS model RID from env."""
    return os.environ.get("CLOUDPSS_MODEL_RID")


@pytest.fixture(scope="session")
def has_cloudpss_token(cloudpss_token):
    """Check if CloudPSS token is available."""
    return cloudpss_token is not None


# ============================================================================
# Network Fixtures (pandapower)
# ============================================================================


@pytest.fixture(scope="session")
def case14_network():
    """Load IEEE case14 network using pandapower."""
    pytest.importorskip("pandapower")
    import pandapower as pp

    net = pp.create_case14()
    return net


@pytest.fixture(scope="session")
def case9_network():
    """Load IEEE case9 network using pandapower."""
    pytest.importorskip("pandapower")
    import pandapower as pp

    net = pp.create_case9()
    return net


@pytest.fixture(scope="session")
def case30_network():
    """Load IEEE case30 network using pandapower."""
    pytest.importorskip("pandapower")
    import pandapower as pp

    net = pp.create_case30()
    return net


# ============================================================================
# JSON Network Fixtures
# ============================================================================


@pytest.fixture
def network_3bus():
    """Load 3-bus test network from JSON."""
    fixture_path = Path(__file__).parent / "fixtures" / "networks" / "3bus_simple.json"
    if fixture_path.exists():
        with open(fixture_path) as f:
            return json.load(f)

    return {
        "name": "3bus_simple",
        "buses": [
            {"name": "Slack", "vn_kv": 110, "type": "slack"},
            {"name": "PQ1", "vn_kv": 110, "type": "pq"},
            {"name": "PQ2", "vn_kv": 110, "type": "pq"},
        ],
        "generators": [
            {"name": "G1", "bus": "Slack", "p_mw": 100, "vm_pu": 1.0, "q_mvar": 20},
        ],
        "loads": [
            {"name": "L1", "bus": "PQ1", "p_mw": 50, "q_mvar": 10},
            {"name": "L2", "bus": "PQ2", "p_mw": 30, "q_mvar": 5},
        ],
        "lines": [
            {
                "name": "L1",
                "from_bus": "Slack",
                "to_bus": "PQ1",
                "length_km": 10,
                "r_ohm_per_km": 0.1,
                "x_ohm_per_km": 0.4,
            },
            {
                "name": "L2",
                "from_bus": "PQ1",
                "to_bus": "PQ2",
                "length_km": 10,
                "r_ohm_per_km": 0.1,
                "x_ohm_per_km": 0.4,
            },
        ],
    }


@pytest.fixture
def network_3bus_as_pp(network_3bus):
    """Convert 3-bus JSON to pandapower network."""
    pytest.importorskip("pandapower")
    import pandapower as pp

    network = network_3bus
    net = pp.create_empty_network()

    for bus in network.get("buses", []):
        pp.create_bus(net, vn_kv=bus["vn_kv"], name=bus["name"])

    for gen in network.get("generators", []):
        bus_idx = next(
            (i for i, b in enumerate(net.bus["name"]) if b == gen["bus"]), None
        )
        if bus_idx is not None:
            pp.create_gen(
                net,
                bus=bus_idx,
                p_mw=gen["p_mw"],
                vm_pu=gen.get("vm_pu", 1.0),
                name=gen["name"],
            )

    for load in network.get("loads", []):
        bus_idx = next(
            (i for i, b in enumerate(net.bus["name"]) if b == load["bus"]), None
        )
        if bus_idx is not None:
            pp.create_load(
                net,
                bus=bus_idx,
                p_mw=load["p_mw"],
                q_mvar=load["q_mvar"],
                name=load["name"],
            )

    for line in network.get("lines", []):
        from_idx = next(
            (i for i, b in enumerate(net.bus["name"]) if b == line["from_bus"]), None
        )
        to_idx = next(
            (i for i, b in enumerate(net.bus["name"]) if b == line["to_bus"]), None
        )
        if from_idx is not None and to_idx is not None:
            pp.create_line_from_to(
                net,
                from_bus=from_idx,
                to_bus=to_idx,
                length_km=line["length_km"],
                r_ohm_per_km=line["r_ohm_per_km"],
                x_ohm_per_km=line["x_ohm_per_km"],
                name=line["name"],
            )

    return net


# ============================================================================
# Mock Result Fixtures
# ============================================================================


@pytest.fixture
def mock_powerflow_result():
    """Load mock power flow result."""
    fixture_path = Path(__file__).parent / "fixtures" / "mock_powerflow_result.json"
    if fixture_path.exists():
        with open(fixture_path) as f:
            return json.load(f)

    return {
        "status": "success",
        "bus_results": [
            {"name": "Slack", "vm_pu": 1.0, "va_deg": 0.0, "p_mw": 100.0},
        ],
    }


@pytest.fixture
def mock_short_circuit_result():
    """Load mock short circuit result."""
    fixture_path = Path(__file__).parent / "fixtures" / "mock_short_circuit_result.json"
    if fixture_path.exists():
        with open(fixture_path) as f:
            return json.load(f)

    return {
        "status": "success",
        "fault_results": [
            {"fault_bus": "PQ1", "ik_sk_ka": 5.2},
        ],
    }


# ============================================================================
# Marker Fixtures
# ============================================================================


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "integration: integration tests requiring external services"
    )
    config.addinivalue_line("markers", "cloudpss: CloudPSS API tests")
    config.addinivalue_line("markers", "pandapower: pandapower tests")
    config.addinivalue_line("markers", "slow: slow tests")
