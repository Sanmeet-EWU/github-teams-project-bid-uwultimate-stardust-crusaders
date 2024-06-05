import ipaddress

from port_scanner import ParsedNmapData

class Machine:
    """"""
    scan_data: ParsedNmapData

    def __init__(self, IP=None, OS=None):
        self.IP = ipaddress.ip_address(IP) if IP else None
        self.OS = OS
        self.vulnerabilities = []
        self.security_rating = 0
        self.color = (199, 36, 177)

    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)

    def attach_scan_data(self, data: ParsedNmapData):
        """"""

    def generate_report(self) -> str:
        '''
        I need some vulnerability report here to return a string and rating. 
        This will be called when you click on the map in network topology.
        '''
        return "This machine is vulnerable"
