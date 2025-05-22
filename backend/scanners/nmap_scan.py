import nmap

def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-T4 -F')
    return nm.csv()