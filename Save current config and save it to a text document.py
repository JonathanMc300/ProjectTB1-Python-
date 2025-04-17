from netmiko import ConnectHandler
import time

start_time = time.time()

sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='172.16.10.150',
    port=22,
    username='admin',
    password='cisco123'
)

# Save running-config to startup-config (handle prompt)
output = sshCli.send_command_timing("copy running-config startup-config")
if "Destination filename" in output:
    output += sshCli.send_command_timing("\n")

# Get running-config
running_config = sshCli.send_command("show running-config")

# Save to file
with open("running_config_output_R1.txt", "w") as file:
    file.write(running_config)

print("Running configuration saved to running_config_output_R1.txt")

sshCli.disconnect()  # Always good to cleanly disconnect

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")