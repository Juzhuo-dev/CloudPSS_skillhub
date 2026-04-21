"""Transient Stability API - Engine-agnostic transient simulation facade.

暂态稳定仿真接口 - 发动机无关的暂态稳定仿真。
"""

from __future__ import annotations

from typing import Any

from cloudpss_skills_v2.powerapi import (
    EngineAdapter,
    SimulationResult,
)
from cloudpss_skills_v2.powerskill.base import SimulationAPI


class TransientStability(SimulationAPI):
    """Lightweight API facade for transient stability simulations."""

    def run_transient(
        self,
        model_handle,
        duration: float = 1.0,
        time_step: float = 0.01,
        fault_location: str | None = None,
        fault_duration: float = 0.1,
        **kwargs,
    ) -> SimulationResult:
        config = {
            "model_handle": model_handle,
            "simulation_type": "transient",
            "duration": duration,
            "time_step": time_step,
            "fault_location": fault_location,
            "fault_duration": fault_duration,
            **kwargs,
        }
        return self._adapter.run_simulation(config)

    def get_generator_angle(self, job_id: str) -> list[dict[str, Any]]:
        result = self._adapter.get_result(job_id)
        if result.data and "generator_angles" in result.data:
            return result.data["generator_angles"]
        return []

    def get_generator_speed(self, job_id: str) -> list[dict[str, Any]]:
        result = self._adapter.get_result(job_id)
        if result.data and "generator_speeds" in result.data:
            return result.data["generator_speeds"]
        return []

    def get_bus_voltage_time_series(self, job_id: str) -> list[dict[str, Any]]:
        result = self._adapter.get_result(job_id)
        if result.data and "voltage_time_series" in result.data:
            return result.data["voltage_time_series"]
        return []


__all__ = ["TransientStability"]
