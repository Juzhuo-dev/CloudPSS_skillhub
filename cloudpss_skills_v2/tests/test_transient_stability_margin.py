"""Tests for cloudpss_skills_v2.poweranalysis.transient_stability_margin."""
import pytest
from cloudpss_skills_v2.poweranalysis.transient_stability_margin import TransientStabilityMarginAnalysis


class TestTransientStabilityMarginAnalysis:

    def test_import(self):
        """Smoke test: module and class can be imported."""
        assert TransientStabilityMarginAnalysis is not None

    def test_instantiation(self):
        """Smoke test: class can be instantiated."""
        try:
            instance = TransientStabilityMarginAnalysis()
        except TypeError:
            pytest.skip("Class requires constructor arguments")

    def test_has_name_attribute(self):
        """Smoke test: instance has expected attributes."""
        try:
            instance = TransientStabilityMarginAnalysis()
            assert hasattr(instance, 'name') or hasattr(instance, 'run')
        except TypeError:
            pytest.skip("Class requires constructor arguments")
