"""DataLib - Analysis result types for PowerAnalysis layer.

Standardized result dataclasses that PowerAnalysis skills return via SkillResult.data.
These replace the untyped dicts that were previously used.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class SeverityLevel(Enum):
    NORMAL = "normal"
    WARNING = "warning"
    CRITICAL = "critical"


@dataclass
class ViolationRecord:
    violation_type: str = ""
    component: str = ""
    value: float = 0.0
    threshold: float = 0.0
    severity: SeverityLevel = SeverityLevel.NORMAL

    def to_dict(self) -> dict[str, Any]:
        return {
            "violation_type": self.violation_type,
            "component": self.component,
            "value": self.value,
            "threshold": self.threshold,
            "severity": self.severity.value,
        }


@dataclass
class ContingencyRecord:
    branch_key: str = ""
    branch_name: str = ""
    converged: bool = False
    severity: SeverityLevel = SeverityLevel.NORMAL
    violations: list[ViolationRecord] = field(default_factory=list)
    min_vm_pu: float | None = None
    max_loading_pct: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "branch_key": self.branch_key,
            "branch_name": self.branch_name,
            "converged": self.converged,
            "severity": self.severity.value,
            "violations": [v.to_dict() for v in self.violations],
            "min_vm_pu": self.min_vm_pu,
            "max_loading_pct": self.max_loading_pct,
        }


@dataclass
class AnalysisSummary:
    total_scenarios: int = 0
    passed: int = 0
    failed: int = 0
    warnings: int = 0
    overall_severity: SeverityLevel = SeverityLevel.NORMAL

    def to_dict(self) -> dict[str, Any]:
        return {
            "total_scenarios": self.total_scenarios,
            "passed": self.passed,
            "failed": self.failed,
            "warnings": self.warnings,
            "overall_severity": self.overall_severity.value,
        }


@dataclass
class SecurityAnalysisResult:
    summary: AnalysisSummary = field(default_factory=AnalysisSummary)
    contingencies: list[ContingencyRecord] = field(default_factory=list)
    violations: list[ViolationRecord] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "summary": self.summary.to_dict(),
            "contingencies": [c.to_dict() for c in self.contingencies],
            "violations": [v.to_dict() for v in self.violations],
        }


@dataclass
class VoltageStabilityResult:
    bus: str = ""
    vsi: float = 0.0
    vm_pu: float = 1.0
    is_weak: bool = False
    margin_pct: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "bus": self.bus,
            "vsi": self.vsi,
            "vm_pu": self.vm_pu,
            "is_weak": self.is_weak,
            "margin_pct": self.margin_pct,
        }


@dataclass
class TheveninResultData:
    pcc_bus: str = ""
    z_th_real_pu: float = 0.0
    z_th_imag_pu: float = 0.0
    z_th_mag_pu: float = 0.0
    scc_mva: float = 0.0
    scr: float = 0.0
    grid_strength: str = "unknown"

    def to_dict(self) -> dict[str, Any]:
        return {
            "pcc_bus": self.pcc_bus,
            "z_th_real_pu": self.z_th_real_pu,
            "z_th_imag_pu": self.z_th_imag_pu,
            "z_th_mag_pu": self.z_th_mag_pu,
            "scc_mva": self.scc_mva,
            "scr": self.scr,
            "grid_strength": self.grid_strength,
        }


@dataclass
class PowerQualityResultData:
    thd: float = 0.0
    thd_threshold: float = 0.05
    thd_exceeds: bool = False
    unbalance: float = 0.0
    unbalance_threshold: float = 0.02
    quality_classification: str = "good"

    def to_dict(self) -> dict[str, Any]:
        return {
            "thd": self.thd,
            "thd_threshold": self.thd_threshold,
            "thd_exceeds": self.thd_exceeds,
            "unbalance": self.unbalance,
            "unbalance_threshold": self.unbalance_threshold,
            "quality_classification": self.quality_classification,
        }


@dataclass
class SensitivityResultData:
    parameter: str = ""
    bus: str = ""
    sensitivity: float = 0.0
    rank: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "parameter": self.parameter,
            "bus": self.bus,
            "sensitivity": self.sensitivity,
            "rank": self.rank,
        }


@dataclass
class BatchResultData:
    model_rid: str = ""
    converged: bool = False
    errors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "model_rid": self.model_rid,
            "converged": self.converged,
            "errors": self.errors,
        }


@dataclass
class BatchAnalysisResult:
    summary: AnalysisSummary = field(default_factory=AnalysisSummary)
    results: list[BatchResultData] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "summary": self.summary.to_dict(),
            "results": [r.to_dict() for r in self.results],
        }


__all__ = [
    "SeverityLevel",
    "ViolationRecord",
    "ContingencyRecord",
    "AnalysisSummary",
    "SecurityAnalysisResult",
    "VoltageStabilityResult",
    "TheveninResultData",
    "PowerQualityResultData",
    "SensitivityResultData",
    "BatchResultData",
    "BatchAnalysisResult",
]
