import socket

def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened "+ str(port))
        sock.close()
    except:
        pass

targets = "192.168.1.1"
ports = 50
if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
