from netmiko import ConnectHandler # imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

start_time = time.time() # Start the timer

sshCli = ConnectHandler( # Establish SSH connection to the device
    device_type='cisco_ios',  # The type of device being connected to
    host='172.16.40.2',     # Device IP address
    port=22,                  # Port number for SSH
    username='admin',         # SSH username
    password='cisco123'       # SSH password
)

config_commands = [ # Define the commands to create VLAN 99 and assign an IP address
    'vlan 99',                                  # Will Create VLAN 99
    'name Netmiko',                             # Will name the VLAN
    'interface vlan 99',                        # Will Enter interface VLAN 99
    'ip address 172.16.99.1 255.255.255.0',     # Will Assign IP address and subnet mask
    'no shutdown',                              # Will Enable the interface
]

output = sshCli.send_config_set(config_commands) # Will send the run the commands from the config_commands

# Stop the timer and calculate the elapsed time
end_time = time.time() # Will stop the timer
elapsed_time = end_time - start_time # Will calculate the time it took to run the code

print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message