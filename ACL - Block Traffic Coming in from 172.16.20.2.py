from netmiko import ConnectHandler # imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

start_time = time.time() # Start the timer

# Connect to the device
sshCli = ConnectHandler(
    device_type='cisco_ios',  # The type of device being connected to
    host='172.16.30.2',       # Device IP address
    port=22,                  # Port number for SSH
    username='admin',         # SSH username
    password='cisco123'       # SSH password
)

# Configuration commands to create ACL that blocks traffic from 172.16.20.2
config_commands = [
    'ip access-list extended Block_Traffic_NetMiko',         # Create an extended ACL named "Block_Traffic"
    'deny ip host 172.16.20.2 any',                  # Deny traffic from 172.16.20.2 to any destination
    'permit ip any any',                             # Permit all other traffic
    'interface GigabitEthernet0/0',                  # Go into interface GigabitEthernet0/1
    'ip access-group Block_Traffic_NetMiko in',              # Apply the ACL to inbound traffic on this interface
]

# Send the configuration commands to the device
sshCli.send_config_set(config_commands)

# Close the SSH connection
sshCli.disconnect()

# Stop the timer and calculate the elapsed time
end_time = time.time() # Will stop the timer
elapsed_time = end_time - start_time # Will calculate the time it took to run the code

print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message