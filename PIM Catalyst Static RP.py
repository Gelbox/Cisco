
import paramiko
from getpass import getpass

# Configuration templates
INTERFACE_CONFIG = """
interface gi1/0/1
 no switchport
 ip address {ip_address} 255.255.255.252
 no shutdown
 ip pim sparse-mode
"""
OSPF_CONFIG = """
router ospf 1
 network 192.168.10.0 0.0.0.255 area 0
 network 192.168.20.0 0.0.0.3 area 0
 network {loopback_ip} 0.0.0.0 area 0
"""
PIM_CONFIG = """
ip multicast-routing
interface vlan 10
 ip pim sparse-mode
ip pim rp-address {rp_address}
"""

# Function to send commands to the device
def send_commands(ssh, commands):
    stdin, stdout, stderr = ssh.exec_command(commands)
    output = stdout.read().decode()
    error = stderr.read().decode()
    if error:
        print(f"Error: {error}")
    return output

# Main script
if __name__ == "__main__":
    # Prompt user for device credentials
    username = input("Enter switch username: ")
    password = getpass("Enter switch password: ")

    # Prompt user for device details
    devices = []
    for i in range(2):
        print(f"Enter details for Switch {i + 1}:")
        ip = input(f"  Management IP address: ")
        loopback_ip = input(f"  Loopback IP address: ")
        gi1_ip = input(f"  Gi1/0/1 IP address: ")
        rp_address = input(f"  RP address: ")

        devices.append({
            "hostname": f"Switch{i + 1}",
            "ip": ip,
            "loopback_ip": loopback_ip,
            "gi1_ip": gi1_ip,
            "rp_address": rp_address
        })

    for device in devices:
        print(f"Configuring {device['hostname']}...")
        
        try:
            # Establish SSH connection
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=device["ip"], username=username, password=password)

            # Build configurations
            interface_config = INTERFACE_CONFIG.format(ip_address=device["gi1_ip"])
            ospf_config = OSPF_CONFIG.format(loopback_ip=device["loopback_ip"])
            pim_config = PIM_CONFIG.format(rp_address=device["rp_address"])

            # Send configurations
            commands = interface_config + ospf_config + pim_config
            output = send_commands(ssh, commands)
            print(output)

            ssh.close()
        except Exception as e:
            print(f"Failed to configure {device['hostname']}: {e}")

    print("Configuration complete.")
