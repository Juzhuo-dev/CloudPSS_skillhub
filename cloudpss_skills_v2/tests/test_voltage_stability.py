"""Tests for cloudpss_skills_v2.poweranalysis.voltage_stability."""
import pytest
from cloudpss_skills_v2.poweranalysis.voltage_stability import VoltageStabilityAnalysis


class TestVoltageStabilityAnalysis:

    def test_import(self):
        """Smoke test: module and class can be imported."""
        assert VoltageStabilityAnalysis is not None

    def test_instantiation(self):
        """Smoke test: class can be instantiated."""
        try:
            instance = VoltageStabilityAnalysis()
        except TypeError:
            pytest.skip("Class requires constructor arguments")

    def test_has_name_attribute(self):
        """Smoke test: instance has expected attributes."""
        try:
            instance = VoltageStabilityAnalysis()
            assert hasattr(instance, 'name') or hasattr(instance, 'run')
        except TypeError:
            pytest.skip("Class requires constructor arguments")
