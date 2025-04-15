from netmiko import ConnectHandler # imports ConnectHandler from netmiko
import time # Will import time so the code can be timed

start_time = time.time() # Start the timer

sshCli = ConnectHandler( # Establish SSH connection to the device
    device_type='cisco_ios', # The type of device being connected to
    host='172.16.10.150', # Device IP address
    port=22, # Port number for SSH
    username='admin', # SSH username
    password='cisco123' # SSH password
)

banner_message = "No Unauthorised Access - NetMiko " # The message that the banner will say
config_commands = [
    "banner motd # {} #".format(banner_message) # The commands to get into the banner
                ]

# Save the running config to startup config
output = sshCli.send_config_set(config_commands)

end_time = time.time() # Will stop the timer
elapsed_time = end_time - start_time #Will calculate the time it took to run the code

print(f"Execution time: {elapsed_time:.4f} seconds") # Will print the time with the following message