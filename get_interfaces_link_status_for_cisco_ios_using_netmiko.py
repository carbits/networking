import time
import sys
from netmiko import ConnectHandler

# import pprint as p

hostnames = ["a.b.c", "e.f.g", "i.j.k"]


# command = "show run"
# command = "show ip int brief\n"
command = "show interfaces link"

username = "xxxx"
password = "yyyy"
port = 22

for hostname in hostnames:
    net_connect = ConnectHandler(device_type='cisco_ios', ip=hostname, username=username, password=password)
    net_connect.find_prompt()
    output = net_connect.send_command(command)
    print(hostname)
    print("------------------")
    print(output)
    print("======================================================================================")
    net_connect.disconnect()

exit()
