import netifaces as ni
import ipaddress
from machine import Machine
import networkx as nx
import matplotlib.pyplot as plt


class NetworkTopology:
    def __init__(self):
        self.machines = {}
        self.host = None
        self.local_ips = self.retrieve_local_ips()

    def add_machine(self, IP, OS="Unknown"):
        try:
            ip = ipaddress.ip_address(IP)

            if str(ip) not in self.machines:
                self.machines[str(ip)] = Machine(IP, OS)
                if str(ip) in self.local_ips:
                    self.host = self.machines[str(ip)]

            else:
                print(f"Machine with IP {IP} already exists in the topology.")
        
        except ValueError:
            print(f"Invalid IP address: {IP}")

    def display_topology(self):
        if not self.machines:
            print("No machines in the topology.")
        nxG = nx.Graph()
        host_node = "127.0.0.1"
        nxG.add_node(host_node)
        x = 1
        for i in range(2,10):
            edge = f"127.0.0.{i}"
            nxG.add_edge(host_node, edge)
        nx.draw(nxG, with_labels=True)
        plt.show()

    def retrieve_local_ips(self):
        ips = []
        interfaces = ni.interfaces()
        for interface in ni.interfaces():
            addrs = ni.ifaddresses(interface)
            ip_info = addrs.get(ni.AF_INET)
            if ip_info:
                ip_address = ip_info[0]['addr']
                ips.append(ip_address)
        return ips



