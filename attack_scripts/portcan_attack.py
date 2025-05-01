from scapy.all import *
import sys

def scan_tcp(destIPs, tcp_ports,all=False):
    print("port scanning started TCP: \n")
    to=1
    try:
        to = float(input("Enter a float value for timeout (by default=1.0 sc), Enter for skip: "))
    except:
        pass
    if (all==True):
        for destIP in destIPs:
            for port in range(tcp_ports[0],tcp_ports[1]):
                send_tcp(port,destIP,to)
    else:
        for destIP in destIPs:
            for port in tcp_ports:
                send_tcp(port,destIP,to)
            
def scan_udp(destIPs, udp_ports,all=False):
    print("port scanning started UDP: \n")
    to=1
    try:
        to = float(input("Enter a float value for timeout (by default=1.0 sc), Enter for skip: "))
    except:
        pass
    if (all==True):
        for destIP in destIPs:
            for port in range(udp_ports[0],udp_ports[1]):
                send_udp(port,destIP,to)
    else:
        for destIP in destIPs:
            for port in udp_ports:
                send_udp(port,destIP,to)

def send_tcp(port,destIP,to=1):
    packet = IP(dst=destIP)/TCP(dport=port, flags='S')
    replay = sr1(packet, timeout=to, verbose=0)

    if replay != None and replay[TCP].flags == 'SA':
        print("The port %s is open at %s" % (port, destIP))

def send_udp(port,destIP,to=1):
    pkt = IP(dst=destIP) / UDP(dport=port)
    resp = sr1(pkt, timeout=to, verbose=0)
    if resp != None:
        if resp.haslayer(UDP) and resp.getlayer(UDP).sport == port:
            print("The port %s is open at %s" % (port, destIP))

def info():
    print("Info:")
    print("default mode which is tcp from port 1 to 5500 : python3 portScan.py ")
    print("---------------------------------------------------")
    print("python3 portScan.py smart")
    print("python3 portScan.py udp smart")
    print("python3 portScan.py udp all")
    print("python3 portScan.py <protocol> <ip_address> <port>")
common_ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 143, 161, 443, 465, 587, 990, 993, 995, 1433, 1521, 3306, 3389,5353, 5432, 5900, 8080]
ip_list =  ['10.12.0.10','10.12.0.20','10.12.0.30','10.12.0.40']


info()

args = sys.argv[1:]
if len(sys.argv) == 1:
    scan_tcp(ip_list, [1,5500],True)
elif len(sys.argv) > 1:
    if args[0] == "smart":
        scan_tcp(ip_list, common_ports)
    elif args[0] == "udp" and args[1] == "smart":
        scan_udp(ip_list, common_ports)
    elif args[0] == "udp" and args[1] == "all":
        scan_udp(ip_list, [1,5500],True)
    elif len(args) == 3:
        protocol = args[0]
        ip_address = args[1]
        port = int(args[2])
        if protocol =="udp":
            scan_udp([ip_address],[port])
        elif protocol=="tcp":
            scan_tcp([ip_address],[port])
    else:
        print("Bad arguments.")
        info()

    


