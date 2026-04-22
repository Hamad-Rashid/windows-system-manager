from __future__ import annotations

from typing import Sequence

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from windows_system_manager.models import (
    BluetoothDeviceEntry,
    PackageEntry,
    PartitionEntry,
    SystemMetrics,
)
from windows_system_manager.providers.base import ProviderBundle
from windows_system_manager.providers.factory import resolve_provider_bundle


class MainWindow(QMainWindow):
    def __init__(self, providers: ProviderBundle) -> None:
        super().__init__()
        self._providers = providers
        self.setWindowTitle("Windows System Manager")
        self.resize(1200, 800)

        tabs = QTabWidget()
        tabs.addTab(self._metrics_tab(), "Metrics")
        tabs.addTab(self._packages_tab(), "Packages")
        tabs.addTab(self._devices_tab(), "Devices")
        tabs.addTab(self._storage_tab(), "Storage")
        tabs.addTab(self._placeholder_tab("Operation logs"), "Logs")
        self.setCentralWidget(tabs)

    def _placeholder_tab(self, title: str) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(f"{title}\n\nImplementation will be added in migration phases.")
        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        label.setWordWrap(True)
        layout.addWidget(label)
        return page

    def _readonly_text_tab(self, title: str, content: str) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(title)
        label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        body = QTextEdit()
        body.setReadOnly(True)
        body.setPlainText(content)
        layout.addWidget(label)
        layout.addWidget(body)
        return page

    def _metrics_tab(self) -> QWidget:
        try:
            metrics = self._providers.system_info.get_metrics()
            return self._readonly_text_tab("System metrics", self._format_metrics(metrics))
        except Exception as exc:  # pragma: no cover - defensive display path
            return self._readonly_text_tab("System metrics", f"Failed to read metrics: {exc}")

    def _packages_tab(self) -> QWidget:
        try:
            packages = self._providers.package_service.list_packages()
            return self._readonly_text_tab("Packages (read-only)", self._format_packages(packages))
        except Exception as exc:  # pragma: no cover - defensive display path
            return self._readonly_text_tab("Packages (read-only)", f"Failed to read packages: {exc}")

    def _devices_tab(self) -> QWidget:
        try:
            devices = self._providers.bluetooth_service.list_devices()
            return self._readonly_text_tab("Bluetooth and USB (read-only)", self._format_devices(devices))
        except Exception as exc:  # pragma: no cover - defensive display path
            return self._readonly_text_tab(
                "Bluetooth and USB (read-only)", f"Failed to read devices: {exc}"
            )

    def _storage_tab(self) -> QWidget:
        try:
            partitions = self._providers.partition_service.list_partitions()
            return self._readonly_text_tab("Partitions and volumes (read-only)", self._format_partitions(partitions))
        except Exception as exc:  # pragma: no cover - defensive display path
            return self._readonly_text_tab(
                "Partitions and volumes (read-only)", f"Failed to read partitions: {exc}"
            )

    def _format_metrics(self, metrics: SystemMetrics) -> str:
        return "\n".join(
            [
                f"Total RAM: {metrics.total_ram}",
                f"Used RAM: {metrics.used_ram}",
                f"Total Storage: {metrics.total_storage}",
                f"Used Storage: {metrics.used_storage}",
            ]
        )

    def _format_packages(self, packages: list[PackageEntry]) -> str:
        if not packages:
            return "No packages available yet. Package provider integration is pending."
        lines = []
        for pkg in packages:
            lines.append(
                f"{pkg.name} | installed={pkg.installed_version} | latest={pkg.latest_version} | status={pkg.status}"
            )
        return "\n".join(lines)

    def _format_devices(self, devices: list[BluetoothDeviceEntry]) -> str:
        if not devices:
            return "No Bluetooth/USB devices available yet. Device provider integration is pending."
        lines = []
        for device in devices:
            status = "connected" if device.connected else "disconnected"
            lines.append(f"{device.name} ({device.address}) - {status}")
        return "\n".join(lines)

    def _format_partitions(self, partitions: list[PartitionEntry]) -> str:
        if not partitions:
            return "No partitions available yet. Storage provider integration is pending."
        lines = []
        for part in partitions:
            lines.append(
                f"{part.device} | fs={part.filesystem} | mount={part.mountpoint} | size={part.size} | status={part.status}"
            )
        return "\n".join(lines)


def run_app(argv: Sequence[str]) -> int:
    app = QApplication(list(argv))
    providers = resolve_provider_bundle()
    win = MainWindow(providers=providers)
    win.show()
    return int(app.exec())
