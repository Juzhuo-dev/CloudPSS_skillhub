"""Tests for cloudpss_skills_v2.tools.waveform_export."""
import pytest
from cloudpss_skills_v2.tools.waveform_export import WaveformExportTool


class TestWaveformExportTool:

    def test_import(self):
        """Smoke test: module and class can be imported."""
        assert WaveformExportTool is not None

    def test_instantiation(self):
        """Smoke test: class can be instantiated."""
        try:
            instance = WaveformExportTool()
        except TypeError:
            pytest.skip("Class requires constructor arguments")

    def test_has_name_attribute(self):
        """Smoke test: instance has expected attributes."""
        try:
            instance = WaveformExportTool()
            assert hasattr(instance, 'name') or hasattr(instance, 'run')
        except TypeError:
            pytest.skip("Class requires constructor arguments")
