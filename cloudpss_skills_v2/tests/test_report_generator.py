"""Tests for cloudpss_skills_v2.tools.report_generator."""
import pytest
from cloudpss_skills_v2.tools.report_generator import ReportGeneratorTool


class TestReportGeneratorTool:

    def test_import(self):
        """Smoke test: module and class can be imported."""
        assert ReportGeneratorTool is not None

    def test_instantiation(self):
        """Smoke test: class can be instantiated."""
        try:
            instance = ReportGeneratorTool()
        except TypeError:
            pytest.skip("Class requires constructor arguments")

    def test_has_name_attribute(self):
        """Smoke test: instance has expected attributes."""
        try:
            instance = ReportGeneratorTool()
            assert hasattr(instance, 'name') or hasattr(instance, 'run')
        except TypeError:
            pytest.skip("Class requires constructor arguments")
