from __future__ import annotations

from windows_system_manager.providers.factory import resolve_provider_bundle
from windows_system_manager.providers.linux.system_info import LinuxSystemInfoProvider
from windows_system_manager.providers.windows.system_info import WindowsSystemInfoProvider


def test_provider_resolution_forced_linux(monkeypatch):
    monkeypatch.setenv("WSM_PROVIDER", "linux")
    bundle = resolve_provider_bundle()
    assert isinstance(bundle.system_info, LinuxSystemInfoProvider)


def test_provider_resolution_forced_windows(monkeypatch):
    monkeypatch.setenv("WSM_PROVIDER", "windows")
    bundle = resolve_provider_bundle()
    assert isinstance(bundle.system_info, WindowsSystemInfoProvider)


def test_provider_resolution_default_matches_platform(monkeypatch):
    monkeypatch.delenv("WSM_PROVIDER", raising=False)
    bundle = resolve_provider_bundle()

    # CI/dev on Linux should resolve to Linux provider by default.
    if __import__("sys").platform.startswith("win"):
        assert isinstance(bundle.system_info, WindowsSystemInfoProvider)
    else:
        assert isinstance(bundle.system_info, LinuxSystemInfoProvider)
