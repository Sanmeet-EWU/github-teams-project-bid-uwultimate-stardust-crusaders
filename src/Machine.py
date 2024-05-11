import ipaddress


class Machine:
    def __init__(self, IP=None, OS=None):
        self.IP = ipaddress.ip_address(IP) if IP else None
        self.OS = OS
        self.vulnerabilities = []
        self.security_rating = 0
        
    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)

    def generate_report(self) -> str:
    '''
    I need some vulnerability report here to return a string and rating. 
    This will be called when you click on the map in network topology.
    '''
        return "This machine is vulnerable"
