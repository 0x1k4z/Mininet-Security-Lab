import os
os.system("sudo nft add table ip filter")
os.system("sudo nft add chain ip filter input { type filter hook input priority 0 \; }")
os.system("sudo nft add set ip filter icmp_blacklist { type ipv4_addr\; flags dynamic,timeout\; timeout 1h \; }") # blacklisted for 1 hour
os.system("sudo nft add rule ip filter input icmp type echo-request limit rate 30/minute add @icmp_blacklist { ip saddr } counter") # limit of 30 ping reques>
os.system("sudo nft add rule ip filter input ip saddr @icmp_blacklist counter drop")




