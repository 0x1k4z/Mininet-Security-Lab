""" Script that creates an nftable for the ftp server to prevent ftp bruteforce attack by limiting the amount
        of tries."""

import os

os.system("sudo nft add table ip filter")
os.system("nft add chain ip filter input { type filter hook input priority 0 \; }")
os.system("nft add set ip filter blacklist { type ipv4_addr\; flags dynamic,timeout\; timeout 12h\; }") # black listed for 12hours to give time to admin to see.
os.system("nft add rule ip filter input ip protocol tcp ct state new, untracked limit rate over 1/minute add @blacklist { ip saddr }")
os.system("nft add rule ip filter input ip saddr @blacklist drop")

