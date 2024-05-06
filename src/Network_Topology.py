import ipaddress
from Machine import Machine


class NetworkTopology:
    def __init__(self):
        self.machines = {}

    def add_machine(self, IP, OS):
        try:
            ip = ipaddress.ip_address(IP)
            if ip not in self.machines:
                self.machines[ip] = Machine(IP, OS)
            else:
                print(f"Machine with IP {IP} already exists in the topology.")
        except ValueError:
            print(f"Invalid IP address: {IP}")

    def display_topology(self):
        if not self.machines:
            print("No machines in the topology.")
        for ip, machine in self.machines.items():
            print(f"IP: {machine.IP}, OS: {machine.OS}")
            if machine.vulnerabilities:
                print("Vulnerabilities:")
                for vulnerability in machine.vulnerabilities:
                    print(vulnerability)
            print()
