"""Small Signal Stability API - Engine-agnostic small signal analysis facade.

小信号稳定分析接口 - 发动机无关的小信号稳定分析。
"""

from __future__ import annotations

from typing import Any

from cloudpss_skills_v2.powerapi import (
    EngineAdapter,
    SimulationResult,
)
from cloudpss_skills_v2.powerskill.base import SimulationAPI


class SmallSignalStability(SimulationAPI):
    """Lightweight API facade for small signal stability analysis."""

    def run_small_signal(
        self,
        model_handle,
        method: str = "eigenvalue",
        **kwargs,
    ) -> SimulationResult:
        config = {
            "model_handle": model_handle,
            "simulation_type": "small_signal",
            "method": method,
            **kwargs,
        }
        return self._adapter.run_simulation(config)

    def get_eigenvalues(self, job_id: str) -> list[complex]:
        result = self._adapter.get_result(job_id)
        if result.data and "eigenvalues" in result.data:
            return result.data["eigenvalues"]
        return []

    def get_participation_factors(self, job_id: str) -> list[dict[str, Any]]:
        result = self._adapter.get_result(job_id)
        if result.data and "participation_factors" in result.data:
            return result.data["participation_factors"]
        return []

    def get_damping_ratios(self, job_id: str) -> list[dict[str, Any]]:
        result = self._adapter.get_result(job_id)
        if result.data and "damping_ratios" in result.data:
            return result.data["damping_ratios"]
        return []

    def get_stability_summary(self, job_id: str) -> dict[str, Any]:
        result = self._adapter.get_result(job_id)
        if result.data and "summary" in result.data:
            return result.data["summary"]
        return {}


__all__ = ["SmallSignalStability"]
