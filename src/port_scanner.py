"""Module containing port scanning related classes and methods."""

import re
import json
from datetime import datetime
from enum import Enum, auto
from typing import TypedDict

import nmap

from vulnerability_lookup.cpe import CPE

class PortState(Enum):
    """Enum representing the state of a port."""
    OPEN = auto()
    CLOSED = auto()
    FILTERED = auto()


class NmapServiceData(TypedDict):
    """Type for parsed nmap data for individual services."""
    cpe: str
    name: str
    state: str


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

    def scan_ports(self) -> tuple[tuple[dict[int, NmapPortData], ...]]:
        if self.host is None:
            raise ValueError("Host not set")

        self.raw_output = self.scanner.scan(
            hosts="scanme.nmap.org",
            arguments='-sV -T4 --open -O')

        return tuple((
            self._parse_scan_host(host)
            for host in self.raw_output['scan'].values()
        ))

    def _parse_scan_host(
            self,
            host_data: dict) -> tuple[dict[int, NmapPortData], ...]:
        """Parse the raw scan data for a host into a usable form.

        Args:
            host_data (object):
                A JSON dictionary containing the parsed data
                from a nmap scan.

        Returns:
            dict[int, NmapPortData]]:
                A dictionary containing relevant nmap data for
                each every port on a given host.
        """
        # This is bad I just want to get this done. TODO come back later...
        tcp_data = {}
        if host_data.get('tcp'):
            for port, port_data in host_data['tcp'].items():
                tcp_data[int(port)] = {
                    'cpe': port_data['cpe'],
                    'name': port_data['name'],
                    'state': (
                        PortState.OPEN if port_data['state'] == 'open' else
                        PortState.CLOSED if port_data['state'] == 'closed' else
                        PortState.FILTERED
                    )
                }
        udp_data = {}
        if host_data.get('udp'):
            for port, port_data in host_data['udp'].items():
                udp_data[int(port)] = {
                    'cpe': port_data['cpe'],
                    'name': port_data['name'],
                    'state': (
                        PortState.OPEN if port_data['state'] == 'open' else
                        PortState.CLOSED if port_data['state'] == 'closed' else
                        PortState.FILTERED
                    )
                }
        os_data = {}
        if host_data.get('osmatch'):
            for os in host_data['osmatch']:
                os_name = os['name']
                os_data[os_name] = {
                    'cpe': os['osclass'][0]['cpe'][0],
                    'name': os_name
                }

        return tcp_data, os_data


def main():
    scanner = PortScanner()
    scanner.set_host("")

    scan_results: tuple[tuple[dict[int, NmapPortData], ...]] = scanner.scan_ports()
    found_with_cpe = 0
    port_cpes: list[tuple[int, CPE]] = []
    os_cpes: list[tuple[str, CPE]] = []
    total_found = 0
    for host_data in scan_results:
        tcp_data = host_data[0]
        os_data = host_data[1]
        for port, port_data in tcp_data.items():
            print(port, port_data['name'], port_data['cpe'])
            if port_data['cpe']:
                port_cpes.append((port, CPE.create_from_str(port_data['cpe'])))
                found_with_cpe += 1
            total_found += 1
        for os, os_data in os_data.items():
            print(os, os_data['name'], os_data['cpe'])
            if os_data['cpe']:
                os_cpes.append((os, CPE.create_from_str(os_data['cpe'])))
                found_with_cpe += 1
            total_found += 1
    if total_found > 0:
        for port, cpe in port_cpes:
            print(f"port:\n {port}", json.dumps(cpe.find_related_cves(), indent=4))
        for os, cpe in os_cpes:
            print(f"os:\n {os}", json.dumps(cpe.find_related_cves(), indent=4))
        print(f"Certainty percentage: {found_with_cpe / total_found * 100}%")
    else:
        print("No results found.")


if __name__ == "__main__":
    main()
