from netmiko import ConnectHandler #imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

# Start the timer
start_time = time.time()

sshCli = ConnectHandler(
    device_type='cisco_ios', # Establish SSH connection to the device
    host='172.16.10.150', # Device IP address
    port=22, # Port number for SSH
    username='admin', # SSH username
    password='cisco123'# SSH password
)

config_commands = [
    'int loopback 10', # Will create loopback 10
    'ip address 10.10.10.10 255.255.255.0', # Will give the loopback the following ip address and subnet
    'description This loopback was created with NetMiko' # Will give it the following description
                ]

output = sshCli.send_config_set(config_commands) # Will send the run the commands from the config_commands

# Stop the timer and calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message