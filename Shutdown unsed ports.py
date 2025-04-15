from netmiko import ConnectHandler
import time

# Start the timer
start_time = time.time()

sshCli = ConnectHandler(
    device_type='cisco_ios', # The type of device being connected to
    host='172.16.40.2', # Device IP address
    port=22, # Port number for SSH
    username='admin', # SSH username
    password='cisco123' # SSH password
)

# Configuration commands to shut down interfaces
config_commands = [
    'interface GigabitEthernet0/1', # Will go into interface G0/1
    'shutdown', # Will shut it down
    'interface GigabitEthernet0/2', # Will go into interface g0/2
    'shutdown', # Will shut it down
    'interface GigabitEthernet0/3', # Will go into interface g0/3
    'shutdown' # Will shut it down
]

# Send the config commands to the device
sshCli.send_config_set(config_commands)

# Print a confirmation message
print("Ports GigabitEthernet0/1, GigabitEthernet0/2, and GigabitEthernet0/3 have been shut down.")

# Stop the timer and calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")