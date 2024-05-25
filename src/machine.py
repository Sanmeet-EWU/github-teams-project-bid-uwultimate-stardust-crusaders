import ipaddress
import random

class Machine:
    def __init__(self, IP=None, OS=None):
        self.IP = ipaddress.ip_address(IP) if IP else None
        self.OS = OS
        self.vulnerabilities = []
        self.security_rating = 0
        self.color = (99,36,177)        
        self.random_color()
    
    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)

    def generate_report(self) -> str:
        '''
        I need some vulnerability report here to return a string and rating. 
        This will be called when you click on the map in network topology.
        '''
        return "This machine is vulnerable"

    def random_color(self):
        red = (255,0,0)
        orange = (255,165,0)
        green = (0,255,0)
        self.color = random.choice([red,orange,green])
