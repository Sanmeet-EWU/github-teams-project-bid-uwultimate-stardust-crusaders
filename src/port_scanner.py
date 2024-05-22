"""Module containing port scanning related classes and methods."""

import subprocess
import re
import json
from datetime import datetime
from typing import TypedDict

import nmap


class NmapServiceData(TypedDict):
    """Type for parsed nmap data for individual services."""
    cpe: str
    title: str


class NmapOSData(TypedDict):
    """Type for parsed nmap data for an OS."""
    cpe: str


class NmapPortData(TypedDict):
    """Type for parsed nmap data for individual ports."""
    services: tuple[NmapServiceData]
    os: NmapOSData


class PortScanner:

    def __init__(self):
        self.host = None
        self.raw_output = None
        self.error_output = None
        self.scanner = nmap.PortScanner()

    def set_host(self, host):
        self.host = host

    def set_port_range(self, port_range=None):
        if port_range is None:
            return ""  # default to 1000 most common
        elif re.match(r"all", port_range, re.IGNORECASE):
            return "-p-"
        else:
            match = re.match(r"(\d+)\s*-\s*(\d+)", port_range)
            if match:
                start_port, end_port = map(int, match.groups())
                if start_port < 1 or end_port > 65535 or start_port > end_port:
                    raise ValueError("Invalid port range")
                return f"-p {start_port}-{end_port}"
            else:
                raise ValueError("Invalid port range format")

    def scan_ports(self, port_range=None):
        if self.host is None:
            raise ValueError("Host not set")

        port_option = self.set_port_range(port_range)

        self.raw_output = self.scanner.scan(
            hosts=self.host,
            ports='1-1000',
            arguments='-sS -sU -A -O -sV')

        return self.raw_output

    def _parse_scan_data(
            self,
            raw_data: dict) -> dict[int, NmapPortData]:
        """Parse the raw scan data into a usable form.

        Args:
            raw_data (object):
                A JSON dictionary containing the parsed data
                from a nmap scan.

        Returns:
            dict[int, NmapPortData]]:
                A dictionary containing relevant nmap data for
                each every port on a given host.
        """
        
        return None

    def save_scan_data(self):
        file_name = f"nmap_scan_{self.host}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(file_name, 'w') as f:
            f.write(self.raw_output)
        print(f"Scan data saved to {file_name}")

    def print_scan_data(self):
        if self.raw_output:
            print("Scan Results:")
            print(json.dumps(self.raw_output.splitlines(), indent=4))
            self.save_scan_data()
        else:
            print("No scan data available")

def main():
    scanner = PortScanner()
    scanner.set_host("127.0.0.1")
    #demo main for testing purposes- hard coded for local host
    #right now it prints the whole scan output. next thing is formatting & parsing it to make it look pretty and extract/save info for cve stuff

    port_range = input("Enter port range (e.g., '1-100', 'all') or press Enter to scan the 1000 most common ports: ") or None

    scan_results = scanner.scan_ports(port_range)
    if scan_results:
        scanner.print_scan_data()
    else:
        print("No results found.")


if __name__ == "__main__":
    main()
