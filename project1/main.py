import scanner
def main():
    print("Welcome to Comprehensive Networking Mapping with Nmap!\n")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            target = input("Enter target IP or range (e.g., 192.168.1.1 or 192.168.1.0/24): ")
            result = scanner.ping_scan(target)
            print_ping_scan_result(result)
        
        elif choice == '2':
            target = input("Enter target IP: ")
            ports = input("Enter ports (e.g., 22-1000, 80, 443): ")
            result = scanner.port_scan(target, ports)
            print_port_scan_result(result)
        
        elif choice == '3':
            target = input("Enter target IP: ")
            result = scanner.host_scan(target)
            if result:  # Check if hosts were found
                print_host_scan_result(result)
            else:
                print(f"No hosts found for {target}")
        
        elif choice == '4':
            target = input("Enter target IP: ")
            result = scanner.os_scan(target)
            print_os_scan_result(result)
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

def print_menu():
    print("Choose an option:")
    print("1. Ping Scan")
    print("2. Port Scan")
    print("3. Host Scan")
    print("4. OS Scan")
    print("5. Exit")

def print_ping_scan_result(result):
    for host in result:
        print(f"Host: {host['host']}")
        print(f"Status: {host['status']}")
        print(f"MAC Address: {host['mac_address']}")
        print(f"Vendor: {host['vendor']}")
        print("Open Ports:")
        for port_info in host['open_ports']:
            print(f"  Port: {port_info['port']}")
            print(f"  State: {port_info['state']}")
            print(f"  Service: {port_info['service']}")
            print()

def print_port_scan_result(result):
    for port_info in result:
        print(f"Host: {port_info['host']}")
        print(f"Port: {port_info['port']}")
        print(f"State: {port_info['state']}")
        print(f"Service: {port_info['service']}")
        print()

def print_host_scan_result(result):
    for host in result:
        print(f"Host: {host['host']}")
        print(f"Status: {host['status']}")
        print(f"MAC Address: {host['mac_address']}")
        if 'hostnames' in host:
            print(f"Hostnames: {host['hostnames']}")
        print(f"Addresses: {host['addresses']}")
        print()

def print_os_scan_result(result):
    for os_info in result:
        print(f"Host: {os_info['host']}")
        print(f"OS Type: {os_info['os_type']}")
        print(f"OS Vendor: {os_info['os_vendor']}")
        print(f"OS Family: {os_info['os_family']}")
        print()



if __name__ == "__main__":
    main()
