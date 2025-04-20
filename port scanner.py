import socket


target = input("Enter the IP address or hostname to scan: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")


try:
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

except socket.gaierror:
    print("\nCouldn’t find host. Check the IP address or hostname.")

except KeyboardInterrupt:
    print("\nScan cancelled by user.")

except socket.error:
    print("\nCould not connect to server.")

print("\nScan complete.")
