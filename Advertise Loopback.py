from netmiko import ConnectHandler # imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

start_time = time.time() # Start the timer

sshCli = ConnectHandler( # Establish SSH connection to the device
    device_type='cisco_ios',  # The type of device being connected to
    host='172.16.10.150',     # Device IP address
    port=22,                  # Port number for SSH
    username='admin',         # SSH username
    password='cisco123'       # SSH password
)

config_commands = [ # Define the commands to create VLAN 99 and assign an IP address
    'router ospf 1',
    'network 10.10.10.10 0.0.0.255 area 0'
]

output = sshCli.send_config_set(config_commands) # Will send the run the commands from the config_commands

# Stop the timer and calculate the elapsed time
end_time = time.time() # Will stop the timer
elapsed_time = end_time - start_time # Will calculate the time it took to run the code

print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message