import ftplib
from Machine import *

class Pen_Tester:
    
    def __init__(self):
        self.exploits = [self.login_to_ftp,]
    

    def run_exploits(self,machine):

        for exploit in self.exploits:
            result = exploit(machine.IP)
        return result        

    def login_to_ftp(self,host):
        try:
            with ftplib.FTP(str(host)) as ftp:
                print("IM TRYING TO LOG IN")
                ftp.login()  
                print("Login successful!")
                return True
        except ftplib.all_errors as e:
            print(f"Failed to connect or login: {e}")
            return False

# Test for demo purposes:
my_machine =  Machine("10.211.55.10","Linux")
pentester =  Pen_Tester()  # Replace with the FTP server's address
result = pentester.run_exploits(my_machine)
print(result)
