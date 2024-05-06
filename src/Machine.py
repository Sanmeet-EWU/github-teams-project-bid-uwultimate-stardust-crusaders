import ipaddress


class Machine:
    def __init__(self, IP=None, OS=None):
        self.IP = ipaddress.ip_address(IP) if IP else None
        self.OS = OS
        self.vulnerabilities = []

    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)
