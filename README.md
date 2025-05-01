# 💻 Network Attacks & Protections

## 📝 Overview

This project demonstrates several common network attacks and their corresponding defenses, implemented in a Mininet-based virtual enterprise network. Each attack script is accompanied by a protection script, ensuring secure and normal operation of the network.

---

## 🔐 Enterprise Network Protection

We enforce the following basic policies using `nftables`:

- 🖥️ **Workstations:** Can initiate connections and ping any host.
- 🌐 **DMZ Servers:** Can only respond to incoming requests; cannot initiate connections or ping.
- 🌍 **Internet Host:** Can only contact DMZ servers.

This simulates a secure enterprise environment.

---

## 💣 Attacks & 🛡️ Defenses

### 1️⃣ ARP Cache Poisoning

**🧪 Scenario:**  
The attacker (ws3) poisons the ARP cache of both the router (r1) and workstation (ws2), pretending to be each other to intercept traffic.

**🚀 Attack:**
```bash
xterm ws2 ws3 r1
# In ws3's terminal:
python3 attack_scripts/arp_cache_poisoning.py
# In ws2:
ping 10.1.0.1
# In r1:
ping 10.1.0.2
```

**🛡️ Defense:**  
Each node verifies IP–MAC pair consistency. If mismatched, packets are dropped.
```bash
# In ws2 and r1:
python3 protection_scripts/arp_cache_poisoning_protection.py
```

---

### 2️⃣ FTP Brute Force Attack

**🧪 Scenario:**  
The attacker (internet) attempts to brute-force login credentials on the FTP server.

**🚀 Attack:**
```bash
xterm internet
python3 attack_scripts/ftp_bruteforce.py
```

**🛡️ Defense:**  
Detection and blocking of repeated failed login attempts.
```bash
xterm ftp
python3 protection_scripts/ftp_bruteforce_protection.py
```

---

### 3️⃣ SYN Flooding Attack

**🧪 Scenario:**  
The attacker floods the HTTP server with half-open TCP connections.

**🚀 Attack:**
```bash
xterm internet
python3 attack_scripts/synflooding_attack.py
```

**🛡️ Defense:**  
The server detects IPs sending more than 20 SYN packets per minute and blocks them for 1 hour.
```bash
xterm http
python3 protection_scripts/synflooding_def.py
```

---

### 4️⃣ Network Scan

**🧪 Scenario:**  
The attacker (internet) scans the internal network to identify live hosts.

**🚀 Attack:**
```bash
xterm internet
python3 attack_scripts/scanIp_attack.py
```

**🛡️ Defense:**  
Limits ICMP Echo Requests (ping) from untrusted sources to DMZ servers.
```bash
xterm dns http ntp ftp
python3 protection_scripts/scanIp_def.py
```

---

### 5️⃣ Port Scan (Extra)

**🧪 Scenario:**  
Performs smart or exhaustive scans on DMZ servers' ports using TCP/UDP.

**🚀 Attack:**
```bash
xterm internet
# Default TCP scan (ports 1–5500):
python3 attack_scripts/portScan.py
# Smart scan (TCP or UDP):
python3 attack_scripts/portScan.py smart
python3 attack_scripts/portScan.py udp smart
# Full UDP scan:
python3 attack_scripts/portScan.py udp all
# Custom:
python3 attack_scripts/portScan.py <protocol> <ip_address> <port>
```

_Note: No protection implemented for this extra attack._

---

## ▶️ How to Run

1. Launch the VM and start the topology:
   ```bash
   sudo -E python3 ~/<FOLDER>/topo.py
   ```

2. Open xterm windows for relevant hosts:
   ```bash
   xterm <host1> <host2> ...
   ```

3. Run the desired attack/protection scripts inside the appropriate host's terminal.

---

## NFT Files 🔥

The `basic_protection_firewalls` directory contains NFT (Netfilter) files designed to protect firewall routers R1 and R2.

---

## 👨‍💻 Authors

- **[hfoudia](https://github.com/0x1k4z)**
- **[amirshehrzad](https://github.com/amirshehrzad)**