from netmiko import ConnectHandler #imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

start_time = time.time() # Start the timer

sshCli = ConnectHandler( # Establish SSH connection to the device
    device_type='cisco_ios', # The type of device being connected to
    host='172.16.10.150', # Device IP address
    port=22, # Port number for SSH
    username='admin', # SSH username
    password='cisco123' # SSH password
)

output = sshCli.send_command_timing("copy running-config startup-config") # Save running-config to startup-config
if "Destination filename" in output:
    output += sshCli.send_command_timing("\n")

# Get running-config
running_config = sshCli.send_command("show running-config") #Will get the running-config


with open("running_config_output_R1.txt", "w") as file: #Will save to the file
    file.write(running_config)

print("Running configuration saved to running_config_output_R1.txt") #Will print a confirmation message

end_time = time.time() # Will stop the timer
elapsed_time = end_time - start_time #Will calculate the time it took to run the code
print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message