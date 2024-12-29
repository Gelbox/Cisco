PIM Sparse Mode Configuration Script

This repository contains a Python script to automate the configuration of PIM Sparse Mode on Layer 3 switches. The script uses SSH to connect to the devices, prompts the user for device details, and applies configurations for interfaces, OSPF, and PIM Sparse Mode, including the Rendezvous Point (RP).
Features

    Configures the following:

        Interface settings (IP address, routed mode, and enabling PIM Sparse Mode).

        OSPF for routing between devices.

        Multicast routing with a manually configured Rendezvous Point (RP).

    Prompts the user to input management IPs, loopback IPs, and other necessary details.

    Supports multiple devices for configuration.

Requirements

    Python 3.6 or higher.

    Paramiko library for SSH communication.

    Install Paramiko using pip:
    pip install paramiko

File Structure
.
├── pim_sparse_mode_config.py    # Main Python script
├── README.md                    # Documentation for the script
Usage

    Clone this repository:
    git clone https://github.com/<your-username>/<your-repo-name>.git
    cd <your-repo-name>

    Run the script:
    python3 pim_sparse_mode_config.py

    Follow the prompts:

        Enter switch credentials (username and password).

        Enter details for each switch (management IP, loopback IP, Gi1/0/1 IP, and RP address).

    The script will establish an SSH connection to each device and apply the configuration.

Example Output
Enter switch username: admin
Enter switch password:
Enter details for Switch 1:
  Management IP address: 192.168.10.1
  Loopback IP address: 1.1.1.1
  Gi1/0/1 IP address: 192.168.20.1
  RP address: 2.2.2.2
Enter details for Switch 2:
  Management IP address: 192.168.10.2
  Loopback IP address: 2.2.2.2
  Gi1/0/1 IP address: 192.168.20.2
  RP address: 2.2.2.2
Configuring Switch 1...
Configuration complete.
Configuring Switch 2...
Configuration complete.
Limitations

    Assumes the devices are accessible via SSH using the provided credentials.

    Limited error handling; ensure devices have SSH enabled and the correct IP configurations.

Contributions

Feel free to fork this repository and submit pull requests for enhancements or bug fixes.
License

This project is licensed under the MIT License. See the LICENSE file for details.




