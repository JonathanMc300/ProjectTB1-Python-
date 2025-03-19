from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='172.16.10.150',
    port=22,
    username='admin',
    password='cisco'
)

output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))