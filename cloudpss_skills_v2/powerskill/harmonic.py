"""Harmonic Analysis API - Engine-agnostic harmonic simulation facade.

谐波分析接口 - 发动机无关的谐波分析。
"""

from __future__ import annotations

from typing import Any

from cloudpss_skills_v2.powerapi import (
    EngineAdapter,
    SimulationResult,
)
from cloudpss_skills_v2.powerskill.base import SimulationAPI


class HarmonicAnalysis(SimulationAPI):
    """Lightweight API facade for harmonic analysis simulations."""

    def run_harmonic(
        self,
        model_handle,
        harmonic_orders: list[int] | None = None,
        frequency_range: tuple[float, float] = (50, 2500),
        **kwargs,
    ) -> SimulationResult:
        config = {
            "model_handle": model_handle,
            "simulation_type": "harmonic",
            "harmonic_orders": harmonic_orders or [2, 3, 5, 7, 9, 11, 13],
            "frequency_range": frequency_range,
            **kwargs,
        }
        return self._adapter.run_simulation(config)

    def get_harmonic_voltages(self, job_id: str) -> list[dict[str, Any]]:
        result = self._adapter.get_result(job_id)
        if result.data and "harmonic_voltages" in result.data:
            return result.data["harmonic_voltages"]
        return []

    def get_harmonic_currents(self, job_id: str) -> list[dict[str, Any]]:
        result = self._adapter.get_result(job_id)
        if result.data and "harmonic_currents" in result.data:
            return result.data["harmonic_currents"]
        return []

    def get_thd(self, job_id: str) -> dict[str, float]:
        result = self._adapter.get_result(job_id)
        if result.data and "thd" in result.data:
            return result.data["thd"]
        return {}


__all__ = ["HarmonicAnalysis"]
