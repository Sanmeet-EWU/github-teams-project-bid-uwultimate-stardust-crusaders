import nmap
import json
import re

class PortScanner:
    
    def __init__(self):
        self.port_scanner = nmap.PortScanner()
        self.host = None
        self.scan_data = None

    def set_host(self, host):
        self.host = host

    def set_port_range(self, port_range):
        if re.match(r"all", port_range, re.IGNORECASE):
            return 1, 65535
        else
            match = re.match(r"(\d+)\s*-\s*(\d+)", port_range)
            if match:
                start_port, end_port = map(int, match.groups())
                if start_port < 1 or end_port > 65535 or start_port > end_port:
                    raise ValueError("Invalid port range")
                return start_port, end_port
            else:
                raise ValueError("Invalid port range format")

    def scan_ports(self, start_port, end_port):
        if self.host is None:
            raise ValueError("Host not set")

        self.scan_data = self.port_scanner.scan(hosts=self.host, ports=f"{start_port}-{end_port}", arguments='-Pn')

        open_ports = []
        for host in self.scan_data['scan']:
            for proto in self.scan_data['scan'][host]['tcp']:
                if self.scan_data['scan'][host]['tcp'][proto]['state'] == 'open':
                    open_ports.append(proto)

        return open_ports

    def print_scan_data(self):
            return print(json.dumps(self.scan_data, indent=4))

