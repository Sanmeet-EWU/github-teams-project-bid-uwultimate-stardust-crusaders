import subprocess
import re


class PortScanner:

    def __init__(self):
        self.host = None
        self.raw_output = None
        self.error_output = None

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

        arguments = f"sudo nmap {self.host} {port_option} -sS -sU -A -O -sV --version-intensity 5 --osscan-guess -Pn"
        print(f"Running command: {arguments}") #can be removed 

        try:
            completed_process = subprocess.run(arguments.split(), capture_output=True, text=True, check=True)
            self.raw_output = completed_process.stdout
            self.error_output = completed_process.stderr
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during scanning: {e}")
            self.raw_output = e.stdout
            self.error_output = e.stderr

        return self.raw_output

    def print_scan_data(self):
        if self.raw_output:
            print("Raw nmap Output:")
            print(self.raw_output)
            if self.error_output:
                print("\nError Output:")
                print(self.error_output)
        else:
            print("No scan data available")


def main():
    scanner = PortScanner()
    scanner.set_host("127.0.0.1")
    #demo main for testing purposes - works on my local host
    #right now it just prints the whole scan output. next thing is formatting and parsing it to make it look pretty and extraxt/save information for cve stuff

    port_range = input(
        "Enter port range (e.g., '1-100', 'all') or press Enter to scan the 1000 most common ports: ") or None

    try:
        scan_results = scanner.scan_ports(port_range)
        if scan_results:
            scanner.print_scan_data()
        else:
            print("No results found.")
    except Exception as e:
        print(f"An error occurred during scanning: {e}")


if __name__ == "__main__":
    main()
