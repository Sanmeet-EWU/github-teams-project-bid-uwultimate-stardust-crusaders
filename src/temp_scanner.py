import nmap

def scan(tgtHost):
    # Initialize the Nmap PortScanner
    nm = nmap.PortScanner()

    # Perform the scan
    nm.scan(hosts=tgtHost, arguments='-A')

    result = {
        'host': tgtHost,
        'ports': [],
        'os_type': None
    }

    # Extract port information
    for proto in nm[tgtHost].all_protocols():
        lport = nm[tgtHost][proto].keys()
        for port in lport:
            state = nm[tgtHost][proto][port]['state']
            if state == 'open' or state == 'filtered':
                service = nm[tgtHost][proto][port].get('name', 'unknown')
                version = nm[tgtHost][proto][port].get('version', 'unknown')
                result['ports'].append({
                    'port': port,
                    'service': service,
                    'version': version
                })

    # Extract OS information
    if 'osclass' in nm[tgtHost]:
        result['os_type'] = nm[tgtHost]['osclass'][0]['osfamily']
    elif 'osmatch' in nm[tgtHost]:
        result['os_type'] = nm[tgtHost]['osmatch'][0]['name']

    return result   
