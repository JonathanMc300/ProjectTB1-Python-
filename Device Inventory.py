from netmiko import ConnectHandler #imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

start_time = time.time() # Start the timer

sshCli = ConnectHandler( # Establish SSH connection to the device
    device_type='cisco_ios', # The type of device being connected to
    host='172.16.10.150', # Device IP address
    port=22,    # Port number for SSH
    username='admin', # SSH username
    password='cisco123' # SSH password
)

config_commands = [ # Commands to retrieve device information
    'show version', # Will run the command show version
    'show inventory', #Will run the command show inventory
    'show run | include hostname' # Will run the command show run and include the host name
]

output = "" # Initialize a variable to store the output

for command in config_commands: # Loop through the commands and collect output

    output += sshCli.send_command(command) + "\n\n"  # Use send_command to execute the show commands and retrieve output

# Save the output to a text file
with open("device_inventory_output.txt", "w") as file:
    file.write(output)

print("Device information saved to device_inventory_output.txt") # Print a message to confirm the file has been written

end_time = time.time() # Will stop the timer
elapsed_time = end_time - start_time #Will calculate the time it took to run the code

print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message