from scapy.all import *
import ipaddress
def scan_subnet(subnet):
    network = ipaddress.ip_network(subnet)
    hosts = network.hosts()
    for host in hosts:
        packet = IP(dst=str(host))/ICMP()
        response = sr1(packet, timeout=1, verbose=0)

        if response is not None:
            print("response from = ",host)
        
subnet = '10.12.0.0/24'
scan_subnet(subnet)

