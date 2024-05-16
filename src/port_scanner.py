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
            return 1, 65535  # Represents the full range of ports.
        else:
            match = re.match(r"(\d+)\s*-\s*(\d+)", port_range)
            if match:
                start_port, end_port = map(int, match.groups())
                if start_port < 1 or end_port > 65535 or start_port > end_port:
                    raise ValueError("Invalid port range")
                return start_port, end_port
            else:
                raise ValueError("Invalid port range format")

    def scan_ports(self, start_port=None, end_port=None):
        if self.host is None:
            raise ValueError("Host not set")

        port_range = f"{start_port}-{end_port}" if start_port and end_port else ""

        arguments = "-sS -sU -A -O -sV --version-intensity 5 --script=default --osscan-guess -Pn"

        self.scan_data = self.port_scanner.scan(hosts=self.host, ports=port_range, arguments=arguments)

        return self.analyze_scan_results()

    def analyze_scan_results(self):
        results = []
        if self.scan_data:
            for host in self.scan_data['scan']:
                host_info = {'host': host}
                for proto in self.scan_data['scan'][host]:
                    host_info[proto] = []
                    for port in self.scan_data['scan'][host][proto]:
                        port_info = self.scan_data['scan'][host][proto][port]
                        host_info[proto].append({
                            'port': port,
                            'state': port_info['state'],
                            'service': port_info.get('name', ''),
                            'product': port_info.get('product', ''),
                            'version': port_info.get('version', ''),
                            'os': self.scan_data['scan'][host].get('osmatch', [])
                        })
                results.append(host_info)
        return results

    def print_scan_data(self):
        if self.scan_data:
            print(json.dumps(self.scan_data, indent=4))
        else:
            print("No scan data available")

    #need to add main for a demo - will do this soon