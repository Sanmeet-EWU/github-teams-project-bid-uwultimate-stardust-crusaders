import ftplib
from machine import *

class Pen_Tester:
    
    def __init__(self):
        self.exploits = [self.login_to_ftp,]
    

    def run_exploits(self,machine):
        report = ""
        for exploit in self.exploits:
            result = exploit(machine.IP)
            if result is not None:
                report += result
        return report 

    def login_to_ftp(self,host):
        try:
            with ftplib.FTP(str(host)) as ftp:
                ftp.login()  
                return "Anonymous FTP Login Enabled\n"
        except ftplib.all_errors as e:
            return None

