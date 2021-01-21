from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host":'cisco3.lasthop.io',
    "username":'pyclass',
    "password": getpass(),
    "device_type":'cisco_ios',
    "session_log": 'my_session_c3.txt'
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

device2 = {
    "host":'cisco4.lasthop.io',
    "username":'pyclass',
    "password": getpass(),
    "device_type":'cisco_ios',
    "session_log": 'my_session_c4.txt'
}

net_connect = ConnectHandler(**device2)
print(net_connect.find_prompt())
output1 = net_connect.send_command("sh ip int brief")
output2 = net_connect.send_command("sh ip arp")
print(output1)
print(output2)
