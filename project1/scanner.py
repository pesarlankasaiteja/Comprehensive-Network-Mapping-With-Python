import nmap
nmap_path ='C:\\Program Files (x86)\\Nmap\\nmap.exe'
nmap.PortScanner.nmap_path = nmap_path
def ping_scan(target):
    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))
    nm.scan(target, arguments='-sV')  # Use -sV for service version detection
    hosts_list = []
    
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            host_details = {
                'host': host,
                'status': nm[host].state(),
                'mac_address': get_mac_address(nm[host]['addresses']),
                'vendor': nm[host]['vendor'],
                'open_ports': []
            }
            
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    port_info = {
                        'port': port,
                        'state': nm[host][proto][port]['state'],
                        'service': nm[host][proto][port]['name']
                    }
                    host_details['open_ports'].append(port_info)
            
            hosts_list.append(host_details)
    
    return hosts_list

def get_mac_address(addresses):
    try:
        return addresses['mac']
    except KeyError:
        return "N/A"

def host_scan(target):
    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))
    nm.scan(target)
    hosts_list = []
    
    if nm.all_hosts():
        for host in nm.all_hosts():
            if nm[host].state() == 'up':
                host_details = {
                    'host': host,
                    'status': nm[host].state(),
                    'hostnames': nm[host]['hostnames'],
                    'addresses': nm[host]['addresses'],
                    'mac_address': get_mac_address(nm[host]['addresses'])
                }
                hosts_list.append(host_details)
    else:
        print(f"No hosts found for {target}")
    
    return hosts_list

def port_scan(target, ports):
    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))
    nm.scan(target, arguments='-sV -p {}'.format(ports))
    
    open_ports = []
    try:
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                if proto == 'tcp':
                    for port in nm[host][proto].keys():
                        port_info = {
                            'host': host,
                            'port': port,
                            'state': nm[host][proto][port]['state'],
                            'service': nm[host][proto][port]['name']
                        }
                        open_ports.append(port_info)
    except KeyError as e:
        print(f"No results found for {target}:{ports}")
    
    return open_ports

def host_scan(target):
    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))
    nm.scan(target)
    hosts_list = []
    
    if nm.all_hosts():
        for host in nm.all_hosts():
            if nm[host].state() == 'up':
                host_details = {
                    'host': host,
                    'status': nm[host].state(),
                    'hostnames': nm[host]['hostnames'],
                    'addresses': nm[host]['addresses'],
                    'mac_address': get_mac_address(nm[host]['addresses'])
                }
                hosts_list.append(host_details)
    else:
        print(f"No hosts found for {target}")
    
    return hosts_list

def os_scan(target):
    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))
    nm.scan(target, arguments='-O')

    os_info_list = []

    try:
        if target in nm.all_hosts() and 'osmatch' in nm[target]:
            os_matches = nm[target]['osmatch']
            for os_match in os_matches:
                os_info = {
                    'host': target,
                    'os_type': os_match['osclass'][0]['osfamily'],
                    'os_vendor': os_match['osclass'][0]['vendor'],
                    'os_family': os_match['osclass'][0]['osfamily']
                }
                os_info_list.append(os_info)
        else:
            print(f"No OS information found for {target}")
    except KeyError as e:
        print(f"Error: {e}")

    return os_info_list



def disable_dns_resolution_scan(target):
    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))
    nm.scan(target, arguments='-n')
    return nm[target]['hostnames'], nm[target]['addresses']
