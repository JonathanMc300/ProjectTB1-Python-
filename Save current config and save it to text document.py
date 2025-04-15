from netmiko import ConnectHandler #imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

# Start the timer
start_time = time.time()

# Establish SSH connection to the device
sshCli = ConnectHandler(
    device_type='cisco_ios',  # The type of device being connected to
    host='172.16.40.2',     # Device IP address
    port=22,                  # Port number for SSH
    username='admin',         # SSH username
    password='cisco123'       # SSH password
)

config_command = 'show running-config' # Command to retrieve the running configuration

output = "" # Initialize a variable to store the output

output += sshCli.send_command(config_command) + "\n\n"  # Execute the command and collect output

with open("running_config_output_SW3.txt", "w") as file:  # Save the output to a text file
    file.write(output)

print("Running configuration saved to running_config_output_SW3.txt") # Print a message to confirm the file has been written

end_time = time.time() # Will stop the timer
elapsed_time = end_time - start_time #Will calculate the time it took to run the code

print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message