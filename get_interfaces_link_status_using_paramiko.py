import time
import sys
import paramiko

hostname = "x.y.z"
my_command = "show interfaces link"

username = "xxxxx"
password = "yyyyy"
port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #client.connect(hostname, port=port, username=username, password=password, look_for_keys=False, allow_agent=False, timeout=20)
    client.connect(hostname, username=username, password=password)

    rem_conxn = client.invoke_shell()
    ab = rem_conxn.send(my_command)
    output = rem_conxn.recv(65535)

    print(ab)
    print(output.decode("utf-8"))

finally:
    client.close()
