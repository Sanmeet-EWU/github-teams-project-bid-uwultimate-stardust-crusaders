import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy, QFormLayout
from PyQt6.QtCore import Qt
from ip_scanner import IPScanner


class ScanOptionsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.ip_scanner = IPScanner()
        self.update_layout("Scan Network")

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                elif child.layout():
                    self.clear_layout(child.layout())

    def update_layout(self, option):
        self.clear_layout(self.layout)
        if option == "Scan Ports":
            self.load_scan_ports_layout()
        elif option == "Scan Network":
            self.load_scan_network_layout()

    def load_scan_ports_layout(self):
        # Create layout for Scan Ports
        scan_ports_layout = QVBoxLayout()

        target_layout = QHBoxLayout()
        target_input = QLineEdit()
        target_input.setPlaceholderText("Target Machine")
        scan_host_button = QPushButton("Scan Host")
        target_layout.addWidget(target_input)
        target_layout.addWidget(scan_host_button)
        scan_ports_layout.addLayout(target_layout)

        # Results Table
        result_table = QTableWidget()
        result_table.setRowCount(4)
        result_table.setColumnCount(3)
        result_table.setHorizontalHeaderLabels(["Service", "Version", "Port"])
        result_table.setItem(0, 0, QTableWidgetItem("SSH"))
        result_table.setItem(0, 1, QTableWidgetItem("2.0"))
        result_table.setItem(0, 2, QTableWidgetItem("22"))
        result_table.setItem(1, 0, QTableWidgetItem("HTTP"))
        result_table.setItem(1, 1, QTableWidgetItem("3.3"))
        result_table.setItem(1, 2, QTableWidgetItem("80"))
        result_table.setItem(2, 0, QTableWidgetItem("FTP"))
        result_table.setItem(2, 1, QTableWidgetItem("1.9"))
        result_table.setItem(2, 2, QTableWidgetItem("21"))
        result_table.setItem(3, 0, QTableWidgetItem("DNS"))
        result_table.setItem(3, 1, QTableWidgetItem("123"))
        result_table.setItem(3, 2, QTableWidgetItem("5300"))

        result_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        scan_ports_layout.addWidget(result_table)

        self.layout.addLayout(scan_ports_layout)

    def load_scan_network_layout(self):
        # Create layout for Scan Network
        scan_network_layout = QVBoxLayout()

        form_layout = QFormLayout()

        ip_label = QLabel("Enter IP Address:    ")
        ip_input = QLineEdit()
        ip_input.setPlaceholderText("Enter IP Address")
        ip_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        subnet_label = QLabel("Enter Subnet Mask:")
        subnet_input = QLineEdit()
        subnet_input.setPlaceholderText("Enter Subnet Mask")
        subnet_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        scan_network_button = QPushButton("Scan Network")
        scan_network_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        ip_layout = QHBoxLayout()
        ip_layout.addWidget(ip_label)
        ip_layout.addWidget(ip_input)

        subnet_layout = QHBoxLayout()
        subnet_layout.addWidget(subnet_label)
        subnet_layout.addWidget(subnet_input)

        form_layout.addRow(ip_layout)
        form_layout.addRow(subnet_layout)
        form_layout.addRow(scan_network_button)

        scan_network_layout.addLayout(form_layout)

        scan_network_button.clicked.connect(lambda: self.on_scan_network_button_clicked(ip_input, subnet_input))

        # Setup result table
        self.result_table = QTableWidget()
        self.result_table.setRowCount(0)
        self.result_table.setColumnCount(1)
        self.result_table.setHorizontalHeaderLabels(["IP Address"])
        self.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        scan_network_layout.addWidget(self.result_table)

        self.layout.addLayout(scan_network_layout)

    def on_scan_network_button_clicked(self, ip_input, subnet_input):
        ip = ip_input.text()
        subnet = subnet_input.text()
        self.scan_network(ip, subnet)

    def scan_network(self, ip, subnet):
        # Call the ip_scanner's scan function
        # self.ip_scanner.scan(ip, subnet)

        # Example: simulate scan results and update the result table
        results = [
            "192.168.1.1",
            "192.168.1.2",
            "192.168.1.3"
        ]
        results.append(ip)
        results.append(subnet)

        # Update the result table with scan results
        self.result_table.setRowCount(len(results))
        for row, ip_address in enumerate(results):
            self.result_table.setItem(row, 0, QTableWidgetItem(ip_address))
