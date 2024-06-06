import ipaddress

from port_scanner import ParsedNmapData, PortScanner, HostCveData

from textwrap import wrap

class Machine:
    """"""
    scan_data: ParsedNmapData
    cve_data: tuple[HostCveData, ...]

    def __init__(self, IP=None):
        self.IP = ipaddress.ip_address(IP) if IP else None
        self.security_rating = 0
        self.color = (255, 255, 255)
        self.cve_data = None

    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)

    def attach_scan_data(self, data: ParsedNmapData):
        """Attach scan data."""
        self.scan_data = data

    def generate_report(self) -> str:
        '''
        I need some vulnerability report here to return a string and rating. 
        This will be called when you click on the map in network topology.
        '''
        if not self.scan_data:
            return "No vulnerabilities found, please run a port scan on this host."
        if not self.cve_data:
            self.cve_data = PortScanner().get_cves_from_scan_data(self.scan_data)
        os_data = None
        vulnerable_data: list[HostCveData] = []
        safe_data = []
        for data in self.cve_data:
            if len(data['cves']) > 0:
                vulnerable_data.append(data)
            elif data['type'] == 'os':
                os_data = data
            else:
                safe_data.append(data)
        result_str = ""
        max_score = 0
        # OS
        result_str += ("-" * 240) + "\n"
        if os_data:
            result_str += f"Operating System: {os_data['identifier']}\n"
            if len(os_data['cves']) > 0:
                result_str += 'Vulnerabilities found:\n'
                result_str += '\n'.join(str(cve) for cve in os_data['cves'])
                result_str += "\n"
            else:
                result_str += "No vulnerabilities found on OS.\n"
            result_str += ("-" * 240) + "\n"
        else:
            result_str += "Could not identify OS.\n"
            result_str += ("-" * 240) + "\n"
        # Vulnerable CVEs
        if len(vulnerable_data) > 0:
            result_str += "Vulnerable services found!\n"
            result_str += ("-" * 240) + "\n"
            for i, data in enumerate(vulnerable_data):
                result_str += f"Vulnerable Service {i}, {data['identifier']}\n"
                result_str += ("-" * 240)
                for i, cve in enumerate(data['cves']):
                    result_str += f'\nVulnerability {i}: ' + str(cve)
                    result_str += "\n"
                    max_score = max(max_score, cve.metrics.base_score)
        else:
            result_str += "No vulnerable services found!\n"
        self.color = (255 * (max_score / 10), 0, 255)
        return "\n".join(wrap(result_str, width=240, replace_whitespace=False))
