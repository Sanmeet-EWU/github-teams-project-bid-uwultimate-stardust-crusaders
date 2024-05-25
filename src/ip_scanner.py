import ipaddress
import nmap
import json

class IPScanner:
    
    def __init__(self):
        
        self.subnet_mask = 24
        self.ip_scanner = nmap.PortScanner()
        self.start_ip = None
        self.end_ip = None


    def set_start_ip(self, new_ip):
        if not self.is_valid_ip(new_ip):
            raise ValueError("Invalid IP Address")
        
        self.start_ip = new_ip


    def set_end_ip(self, new_ip):
        if not self.is_valid_ip(new_ip):
            raise ValueError("Invalid IP Address")
        
        self.end_ip = new_ip
   

    def set_subnet(self, new_subnet):
        if new_subnet < 8 or new_subnet > 31:
            raise ValueError("Invalid Subnet Mask")
        
        self.subnet_mask = new_subnet
        

    def is_valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False


    def scan_subnet(self,ip, subnet):
        ip_range = f"{ip}/{subnet}"
        results = self.ip_scanner.scan(hosts=ip_range, arguments='-sn')
        alive_host = []

        scan_data = results['scan']
        for host, details in scan_data.items():
            if details['status']['state'] == 'up':
                alive_host.append(details['addresses']['ipv4'])

        return alive_host


    def scan_range(self):
        
        octets = self.end_ip.split(".")
        ip_range = self.start_ip + "-" + octets[-1]
        
        alive_host = ""

        results = self.ip_scanner.scan(hosts=ip_range, arguments='-sn')
        
        for host, details in scan_data.items():
            print(details)
            if details['status']['state'] == 'up':
                alive_host += details['addresses']['ipv4'] + "\n"
                print(f"Host {details['addresses']['ipv4']} is up")

        return alive_host


