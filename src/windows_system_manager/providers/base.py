from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from windows_system_manager.models import (
    BluetoothDeviceEntry,
    PackageEntry,
    PartitionEntry,
    SystemMetrics,
)


@dataclass(slots=True)
class ActionResult:
    ok: bool
    message: str


class SystemInfoProvider(ABC):
    @abstractmethod
    def get_metrics(self) -> SystemMetrics:
        raise NotImplementedError


class PackageServiceProvider(ABC):
    @abstractmethod
    def list_packages(self) -> list[PackageEntry]:
        raise NotImplementedError


class PackageActionsProvider(ABC):
    @abstractmethod
    def update_all(self) -> ActionResult:
        raise NotImplementedError

    @abstractmethod
    def update_package(self, package_name: str) -> ActionResult:
        raise NotImplementedError

    @abstractmethod
    def remove_package(self, package_name: str) -> ActionResult:
        raise NotImplementedError


class BluetoothServiceProvider(ABC):
    @abstractmethod
    def list_devices(self) -> list[BluetoothDeviceEntry]:
        raise NotImplementedError


class PartitionServiceProvider(ABC):
    @abstractmethod
    def list_partitions(self) -> list[PartitionEntry]:
        raise NotImplementedError


class PartitionActionsProvider(ABC):
    @abstractmethod
    def mount(self, device: str) -> ActionResult:
        raise NotImplementedError

    @abstractmethod
    def unmount(self, device: str) -> ActionResult:
        raise NotImplementedError

    @abstractmethod
    def repair(self, device: str) -> ActionResult:
        raise NotImplementedError


@dataclass(slots=True)
class ProviderBundle:
    system_info: SystemInfoProvider
    package_service: PackageServiceProvider
    package_actions: PackageActionsProvider
    bluetooth_service: BluetoothServiceProvider
    partition_service: PartitionServiceProvider
    partition_actions: PartitionActionsProvider
