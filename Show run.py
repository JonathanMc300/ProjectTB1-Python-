from netmiko import ConnectHandler #imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

# Start the timer
start_time = time.time()

# Establish SSH connection to the device
sshCli = ConnectHandler(
    device_type='cisco_ios',  # The type of device being connected to
    host='172.16.10.150',     # Device IP address
    port=22,                  # Port number for SSH
    username='admin',         # SSH username
    password='cisco123'       # SSH password
)

config_command = 'do show run' # Command to show the running configuration

output = sshCli.send_config_set(config_command) # Will send the run the commands from the config_commands
print("show run\n{}\n".format(output))

# Stop the timer and calculate the elapsed time
end_time = time.time() # Will stop the timer
elapsed_time = end_time - start_time # Will calculate the time it took to run the code

print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message