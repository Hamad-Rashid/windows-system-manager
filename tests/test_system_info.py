from __future__ import annotations

from windows_system_manager.providers.linux.system_info import LinuxSystemInfoProvider


def test_linux_system_metrics_shape():
    provider = LinuxSystemInfoProvider()
    metrics = provider.get_metrics()

    assert metrics.total_ram
    assert metrics.used_ram
    assert metrics.total_storage
    assert metrics.used_storage

    assert metrics.total_ram.endswith("GiB")
    assert metrics.used_ram.endswith("GiB")
    assert metrics.total_storage.endswith("GiB")
    assert metrics.used_storage.endswith("GiB")
