import os

os.system("sudo nft add table ip filter")
os.system("sudo nft add chain ip filter input { type filter hook input priority 0 \; }")
os.system("sudo nft add set ip filter blacklist { type ipv4_addr\; flags dynamic,timeout\; timeout 1h \; }") # black listed for 1 minute
os.system("sudo nft add rule ip filter input tcp flags syn limit rate over 20/minute add @blacklist { ip saddr } counter")
os.system("sudo nft add rule ip filter input ip saddr @blacklist counter drop")
