import ipaddress

class Ip_Scanner:

    def __init__(self):
        self.start_ip = None
        self.end_ip = None
        self.subnet_mark = 24

    def set_start_ip(self, ip: ipaddress) -> None:
        if not is_valid_ip(ip):
            raise TypeError("Invald IP Address")

        self.start_ip = ip
    
    def set_end_ip(self, ip: ipaddress) -> None:
        if not is_valid_ip(ip):
            raise ValueError("Invald IP Address")

        self.end_ip = ip

    def is_valid_ip(self, ip: ipaddress):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    

