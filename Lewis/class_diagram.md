@startuml
class IP_Scanner {
subnet_mask : String
start_ip : IP
end_ip : IP
scan_ip()
}

class Port_Scanner {
ports : int []
scan_flag : string
ip : IP
scan_ports()
os_detection()
service_detection()
}

class IP {
ip: String
}

class Network_Topology {
topology: Machine []
display_topology()
}

class Machine {
ip : IP
os : String
vulnerabilities: Vulnerabilities
}

IP_Scanner *-- IP
Port_Scanner *--IP
Machine *-- IP
Network_Topology *-- Machine
Machine *-- Vulnerabilities
Exploit *-- Machine
class Hashes {
identify_hashes()
crack_hashes()
time_to_crack()
display_times()
}

class Vulnerabilities {
vulnerabilites : String []
identify_vulnerability()
add_vulnerability()
delete_vulnerability()

}

class Exploit {
machines: Machine []
exploit()
}


@enduml


