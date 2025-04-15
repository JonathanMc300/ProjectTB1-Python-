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

output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))

# Stop the timer and calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")