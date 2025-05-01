""" Python script that defends against arp spoofing attacks by implementing static arp tables with nftables. """
import os

# Read in the IP-MAC pairs from the file
with open('addresses.txt', 'r') as f:
    lines = f.readlines()

os.system("sudo nft add table ip filter")
os.system("nft add chain ip filter input { type filter hook input priority 0 \; }")

# Loop over each line in the file.
for line in lines:
    ip, mac = line.strip().split('-')

    command = f"nft add rule ip filter input ip saddr {ip} ether saddr != {mac} drop"
    os.system(command)

