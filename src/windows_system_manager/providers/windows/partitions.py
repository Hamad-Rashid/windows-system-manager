from __future__ import annotations

from windows_system_manager.models import PartitionEntry
from windows_system_manager.providers.base import (
    ActionResult,
    PartitionActionsProvider,
    PartitionServiceProvider,
)


class WindowsPartitionServiceProvider(PartitionServiceProvider):
    def list_partitions(self) -> list[PartitionEntry]:
        return []


class WindowsPartitionActionsProvider(PartitionActionsProvider):
    def mount(self, device: str) -> ActionResult:
        return ActionResult(False, f"Not implemented yet for mount '{device}'.")

    def unmount(self, device: str) -> ActionResult:
        return ActionResult(False, f"Not implemented yet for unmount '{device}'.")

    def repair(self, device: str) -> ActionResult:
        return ActionResult(False, f"Not implemented yet for repair '{device}'.")
