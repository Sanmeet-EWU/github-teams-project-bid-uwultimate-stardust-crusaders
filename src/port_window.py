import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, \
    QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy, QFormLayout, QListWidget, QMessageBox
from PyQt6.QtCore import Qt
from ip_scanner import IPScanner
from network_topology import *
from temp_scanner import *


class PortOptionsWidget(QWidget):
    def __init__(self, network):
        super().__init__()
        self.network = network
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.ip_scanner = IPScanner()
        self.load_port_layout()

    def load_port_layout(self):
        # Create layout for Scan Ports
        scan_ports_layout = QVBoxLayout()

        target_layout = QHBoxLayout()
        target_input = QLineEdit()
        range_input1= QLineEdit()
        range_input2 = QLineEdit()
        range_label = QLabel()
        to_label = QLabel()

        # Dropdown Box
        service_combo = QComboBox()
        service_combo.addItems(self.network.machines.keys())
#        self.service_combo.currentIndexChanged.connect(self.update_result_table)
        service_combo.showEvent = lambda event: self.update_service_combo(service_combo)
        scan_ports_layout.addWidget(service_combo)

        range_label.setText("Range:")
        to_label.setText("to")
        target_input.setPlaceholderText("Target Machine")
        scan_host_button = QPushButton("Scan Host")
        target_layout.addWidget(target_input)
        target_layout.addWidget(range_label)
        target_layout.addWidget(range_input1)
        target_layout.addWidget(to_label)
        target_layout.addWidget(range_input2)
        target_layout.addWidget(scan_host_button)
        scan_ports_layout.addLayout(target_layout)

        # Results Table
        self.result_table = QTableWidget()
        self.result_table.setRowCount(4)
        self.result_table.setColumnCount(3)
        self.result_table.setHorizontalHeaderLabels(["Service", "Version", "Port"])


        self.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        scan_host_button.clicked.connect(lambda: self.on_scan_host_clicked(service_combo, target_input, range_input1, range_input2))
        scan_ports_layout.addWidget(self.result_table)

        self.layout.addLayout(scan_ports_layout)

    def on_scan_host_clicked(self, service_combo, target_input, range_input1, range_input2):
        target_ip = target_input.text().strip()
        port_range= range_input1.text()+"-"+range_input2.text()
        if not target_ip:
            target_ip = service_combo.currentText().strip()
        if target_ip:
            results = scan(target_ip,port_range)
            if results and results['ports']:
                self.result_table.setRowCount(0)  # Clear previous results
                for port_info in results['ports']:
                    row_position = self.result_table.rowCount()
                    self.result_table.insertRow(row_position)
                    self.result_table.setItem(row_position, 0, QTableWidgetItem(port_info['service']))
                    self.result_table.setItem(row_position, 1, QTableWidgetItem(port_info['version']))
                    self.result_table.setItem(row_position, 2, QTableWidgetItem(str(port_info['port'])))
            else:
                QMessageBox.warning(None, "Scan Error", "No open or filtered ports found.")
        else:
            QMessageBox.warning(None, "Input Error", "Please select a target machine or enter an IP address.")


    def update_service_combo(self, combo_box):
        combo_box.clear()
        combo_box.addItems(self.network.machines.keys())
