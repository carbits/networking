import time
import sys
from netmiko import ConnectHandler

hostnames = ["host1", "host2", "host3", "host4", "host5"]

command = "show interfaces link"

username = "xxxx"
password = "yyyy"

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
