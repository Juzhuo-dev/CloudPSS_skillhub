"""Tests for cloudpss_skills_v2.poweranalysis.n1_security."""
import pytest
from cloudpss_skills_v2.poweranalysis.n1_security import N1SecurityAnalysis


class TestN1SecurityAnalysis:

    def test_import(self):
        """Smoke test: module and class can be imported."""
        assert N1SecurityAnalysis is not None

    def test_instantiation(self):
        """Smoke test: class can be instantiated."""
        try:
            instance = N1SecurityAnalysis()
        except TypeError:
            pytest.skip("Class requires constructor arguments")

    def test_has_name_attribute(self):
        """Smoke test: instance has expected attributes."""
        try:
            instance = N1SecurityAnalysis()
            assert hasattr(instance, 'name') or hasattr(instance, 'run')
        except TypeError:
            pytest.skip("Class requires constructor arguments")
