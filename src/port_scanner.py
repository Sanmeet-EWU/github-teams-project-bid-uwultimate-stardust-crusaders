"""Module containing port scanning related classes and methods."""

import re
from enum import Enum, auto
from typing import TypedDict

import nmap

from vulnerability_lookup.cpe import CPE
from vulnerability_lookup.cve import CVE


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
    product: str
    version: str
    state: str


class NmapOSData(TypedDict):
    """Type for parsed nmap data for an OS."""
    cpe: CPE | None
    name: str


class ParsedNmapData(TypedDict):
    tcp: dict[int, NmapPortData]
    udp: dict[int, NmapPortData]
    os: NmapOSData | None


class HostCveData(TypedDict):
    identifier: str
    type: str
    cpe: CPE
    cves: tuple[CVE, ...]


class NmapDataParser:
    def __init__(self, data: object):
        self._data = data

    def parse(self) -> dict[str, ParsedNmapData]:
        return {
            host:
            {
                'tcp': self._parse_protocol(data, 'tcp'),
                'udp': self._parse_protocol(data, 'udp'),
                'os': self._parse_os(data),
            }
            for host, data in self._data['scan'].items()
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
                    'product': port_data['product'],
                    'version': port_data['version'],
                    'state': (
                        PortState(port_data['state']) if
                        port_data['state'] in (
                            state.value for state in PortState) else
                        PortState.UNKNOWN
                    )
                }
        return results

    def _parse_os(self, data: object) -> dict[str, NmapOSData]:
        if os_data := data.get('osmatch'):
            if first_os := os_data[0]:
                os_name = first_os['name']
                cpe = ""
                if len(os_class := first_os['osclass']) > 0:
                    if len(os_cpes := os_class[0].get('cpe')) > 0:
                        cpe = os_cpes[0]
                return {
                    'cpe': CPE.create_from_str(cpe),
                    'name': os_name
                }
        return {}


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
            host: str = "scanme.nmap.org",
            port_start: int = 0,
            port_end: int = 65355) -> ParsedNmapData:
        return NmapDataParser(
            self.scanner.scan(
                hosts=host,
                arguments='-sV -T4 -O',
                ports=f'{port_start}-{port_end}'
            )
        ).parse()

    def get_cves_from_scan_data(
            self,
            data: ParsedNmapData,
            max_cves_per_cpe: int = 10) -> tuple[HostCveData, ...]:
        results: list[HostCveData] = []
        for host_data in data.values():
            for key, data in host_data.items():
                if key in ['tcp', 'udp']:
                    for port, port_data in data.items():
                        if port_data.get('cpe'):
                            results.append(
                                {
                                    'identifier': port,
                                    'type': key,
                                    'cpe': port_data['cpe'],
                                    'cves': port_data['cpe'].find_related_cves(
                                        max_cves=max_cves_per_cpe)
                                }
                            )
                else:
                    if data.get('cpe'):
                        results.append(
                            {
                                'identifier': data['name'],
                                'type': 'os',
                                'cpe': data['cpe'],
                                'cves': data['cpe'].find_related_cves(
                                    max_cves=max_cves_per_cpe
                                )
                            }
                        )
        return tuple(results)


def main():
    scanner = PortScanner()
    scanner.set_host("")

    scan_results: ParsedNmapData = scanner.scan_ports()
    scanner.get_cves_from_scan_data(scan_results)


if __name__ == "__main__":
    main()
