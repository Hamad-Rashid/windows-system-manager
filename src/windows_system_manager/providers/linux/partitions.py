from __future__ import annotations

import psutil

from windows_system_manager.models import PartitionEntry
from windows_system_manager.providers.base import (
    ActionResult,
    PartitionActionsProvider,
    PartitionServiceProvider,
)


def _bytes_to_gib_text(value: int) -> str:
    gib = value / (1024**3)
    return f"{gib:.1f} GiB"


class LinuxPartitionServiceProvider(PartitionServiceProvider):
    def list_partitions(self) -> list[PartitionEntry]:
        entries: list[PartitionEntry] = []
        for part in psutil.disk_partitions(all=False):
            try:
                usage = psutil.disk_usage(part.mountpoint)
                size = _bytes_to_gib_text(usage.total)
            except PermissionError:
                size = "unknown"
            entries.append(
                PartitionEntry(
                    device=part.device,
                    filesystem=part.fstype,
                    mountpoint=part.mountpoint,
                    expected_mountpoint=part.mountpoint,
                    size=size,
                    status="mounted",
                    status_detail="Read-only parity mode",
                    can_mount=False,
                    can_fix=False,
                )
            )
        return entries


class LinuxPartitionActionsProvider(PartitionActionsProvider):
    def mount(self, device: str) -> ActionResult:
        return ActionResult(False, f"Linux mount action is not implemented for '{device}'.")

    def unmount(self, device: str) -> ActionResult:
        return ActionResult(False, f"Linux unmount action is not implemented for '{device}'.")

    def repair(self, device: str) -> ActionResult:
        return ActionResult(False, f"Linux repair action is not implemented for '{device}'.")
