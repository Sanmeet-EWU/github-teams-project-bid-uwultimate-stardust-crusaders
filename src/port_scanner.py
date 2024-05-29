"""Module containing port scanning related classes and methods."""

import re
from enum import Enum, auto
from typing import TypedDict

import nmap

from vulnerability_lookup.cpe import CPE


class PortState(Enum):
    """Enum representing the state of a port."""
    OPEN = 'open'
    CLOSED = 'closed'
    FILTERED = 'filtered'
    UNKNOWN = auto()


class NmapPortData(TypedDict):
    """Type for parsed nmap data for individual ports."""
    cpe: CPE | None
    name: str
    state: str


class NmapOSData(TypedDict):
    """Type for parsed nmap data for an OS."""
    cpe: CPE | None
    name: str


class ParsedNmapData(TypedDict):
    tcp: dict[int, NmapPortData]
    udp: dict[int, NmapPortData]
    os: NmapOSData | None


class NmapDataParser:
    def __init__(self, data: object):
        self._data = data

    def parse(self) -> ParsedNmapData:
        return {
            'tcp': self._parse_protocol(self._data['scan'], 'tcp'),
            'udp': self._parse_protocol(self._data['scan'], 'udp'),
            'os': self._parse_os(self._data['scan']),
        }

    def _parse_protocol(
            self,
            data: object,
            protocol: str) -> dict[int, NmapPortData]:
        results = {}
        if protocol_data := data.get(protocol):
            for port, port_data in protocol_data.items():
                results[int(port)] = {
                    'cpe': CPE.create_from_str(port_data['cpe']),
                    'name': port_data['name'],
                    'state': (
                        PortState(port_data['state']) if
                        port_data['state'] in (
                            state.value for state in PortState) else
                        PortState.UNKNOWN
                    )
                }
        return results

    def _parse_os(self, data: object) -> dict[str, NmapOSData]:
        results = None
        if os_data := data.get('osmatch'):
            if first_os := os_data[0]:
                os_name = first_os['name']
                cpe = ""
                if len(os_class := first_os['osclass']) > 0:
                    if len(os_cpes := os_class[0].get('cpe')) > 0:
                        cpe = os_cpes[0]
                os_data[os_name] = {
                    'cpe': CPE.create_from_str(cpe),
                    'name': os_name
                }
        return results


class PortScanner:

    def __init__(self):
        self.host = None
        self.raw_output = None
        self.error_output = None
        self.scanner = nmap.PortScanner()

    def set_host(self, host):
        self.host = host

    def scan_ports(
            self,
            port_start: int = 0,
            port_end: int = 65355) -> ParsedNmapData:
        if self.host is None:
            raise ValueError("Host not set")
        return NmapDataParser(
            self.scanner.scan(
                hosts="scanme.nmap.org",
                arguments='-sV -T4 --open -O',
                ports=f'{port_start}-{port_end}'
            )
        ).parse()


def main():
    scanner = PortScanner()
    scanner.set_host("")

    scan_results: ParsedNmapData = scanner.scan_ports()
    for key, data in scan_results.items():
        if key in ['tcp', 'udp']:
            for port, port_data in data[key].items():
                cves = port_data['cve'].find_related_cves(results=100)
                print(f"Port: {port}, CVEs:\n- " + "\n- ".join(
                    str(cve) for cve in cves))
        else:
            cves = data['cve'].find_related_cves()
            print(f"Port: {data['name']}, CVEs:\n- " + "\n- ".join(
                    str(cve) for cve in cves))


if __name__ == "__main__":
    main()
