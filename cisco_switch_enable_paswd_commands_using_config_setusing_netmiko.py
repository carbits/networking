import datetime
import csv
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException

input_csv_file = "cisco_switch_config_set_enable_input.csv"
output_file = open("cisco_switch_config_set_enable_output.txt", "a")

if __name__ == "__main__":
    with open(input_csv_file) as csvfile:
        csv_lines = csv.reader(csvfile, delimiter=',')
        next(csv_lines)  # skip header, the first row
        csv_list = list(csv_lines)

    IPs = [item[0] for item in csv_list]  # get only IPs and ignore other fields

    username = "xxxxx"
    password = "yyyyy"

    command = "enable"
    config_commands = ["conf t",
                       "username net_engr password aaaaaaa privilege 15",
                       "no enable password",
                       "enable password bbbbbbbb",
                       "exit"]
    for my_ip in IPs:
        try:
            net_connect = ConnectHandler(device_type='cisco_ios', ip=my_ip, username=username, password=password)
        except NetMikoTimeoutException:
            output_file.write("{0}{1}".format(my_ip, "== could not connect\n"))
            continue

        net_connect.find_prompt()
        output = net_connect.send_command(command)
        output_file.write(str(datetime.datetime.now()) + "\n")
        output_file.write(my_ip + "\n")
        output_file.write("------------------ \n")
        output_file.write(output)

        net_connect.enable()
        net_connect.find_prompt()
        output_file.write("------------------ \n")
        output1 = net_connect.send_config_set(config_commands)
        output_file.write(output1)
        output_file.write("======================================================================================\n")
        net_connect.disconnect()

output_file.close()
exit()
