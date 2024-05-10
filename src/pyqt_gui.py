from ip_scanner import *
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QTabWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6 import uic
class MyApp(QTabWidget):
    def __init__(self):
        super().__init__()
        self.IP_Scanner = IPScanner()
        uic.loadUi('scanmasterx.ui',self)        

        # if uic works this can be removed   
        '''
        self.setWindowTitle("ScanMasterX")
        self.setWindowIcon(QIcon('scanmasterx.ico'))
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.inputField = QLineEdit()
        button = QPushButton('&Enter IP', clicked=self.scan_subnet)
        self.output = QTextEdit ()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)
        '''
    def scan_subnet(self):
        ipaddress = self.inputField.text()
        self.IP_Scanner.set_start_ip(ipaddress)
        results = self.IP_Scanner.scan_subnet()
        self.output.setText(results)




app = QApplication([])
window = MyApp()
window.show()
app.exec()

