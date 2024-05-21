import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QTabWidget

class ScanMasterX(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scan Master X")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        main_layout = QVBoxLayout()

        # Tabs
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)

        # Scan Tab
        scan_tab = QWidget()
        scan_layout = QVBoxLayout()
        scan_tab.setLayout(scan_layout)

        # Scan Ports Dropdown
        scan_ports_combo = QComboBox()
        scan_ports_combo.addItem("Scan Ports")
        scan_ports_combo.addItem("Scan Network")
        scan_layout.addWidget(scan_ports_combo)

        # Target Machine Input and Scan Host Button
        target_layout = QHBoxLayout()
        target_input = QLineEdit()
        target_input.setPlaceholderText("Target Machine")
        scan_host_button = QPushButton("Scan Host")
        target_layout.addWidget(target_input)
        target_layout.addWidget(scan_host_button)
        scan_layout.addLayout(target_layout)

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

        result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        scan_layout.addWidget(result_table)

        tab_widget.addTab(scan_tab, "Scan")

        # Display Topology Tab
        display_topology_tab = QWidget()
        display_topology_layout = QVBoxLayout()
        display_topology_tab.setLayout(display_topology_layout)
        # Add content to Display Topology Tab as needed
        display_topology_layout.addWidget(QLabel("Display Topology content goes here"))
        tab_widget.addTab(display_topology_tab, "Display Topology")

        # Exploit Tab
        exploit_tab = QWidget()
        exploit_layout = QVBoxLayout()
        exploit_tab.setLayout(exploit_layout)
       
        exploit_layout.addWidget(QLabel("Exploit content goes here"))
        tab_widget.addTab(exploit_tab, "Exploit")

        # Set main layout
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

def main():
    app = QApplication(sys.argv)
    window = ScanMasterX()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
