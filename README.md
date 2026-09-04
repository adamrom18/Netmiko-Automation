# Netmiko-Automation
Using netmiko to automate network devices.

# The Purpose
Learn network automation using python and particularly the netmiko library to gain a better understanding of networks at scale and tools used.

# What does the script do?
loopback_creation.py was my starting point after completing a Cisco networking lab which I added upon to create spine-leaf-connection.py.
The primary purpose is to configure a 5 MLS Spine and Leaf topology by:
  1. SSH into each device.
  2. Configure switchport interfaces to routing ports and adds an ip address.
  3. Adds needed OSPF routes to facilitate cross spine & leaf and vlan communication. 
  4. Sets up Vlans and SVIs on the leaf switches.
  5. Configures access ports and associated vlans on leaf switches.
A network engineer would only need to change the json info to suit the addressing.

# Use case
Expanding a datacenter rapidly without needing to configure each device one by one. The script is also easily adaptable to
handle additional devices/interfaces or adding an additional module such as ACL configuration.

# Upcoming changes
  1. Pre-change validation
  2. Configuration backup
  3. Proper post-change validation
  4. Rollbacks
  5. Logging rather than print
# Future features
  1. Idempotent architecture (Current state -> Desired state -> Change required only)
  2. Dry-run

# Lessons Learned
1. Navigating through json hierarchy with python. 
2. Structuring the script into modules to allow differing configuration without rewriting the code.
3. The Spine & Leaf topology itself. Particularly that it uses layer 3 links rather than layer 2 trunk lines.
4. Using CML2 which has more features than Packet Tracer but constrains you to only 5 managed devices (had to make them count). 
5. Dedicated out-of-band management lines to separate management traffic from the main network while also 
   being an assurance that if the main network fails you can still configure the device.
6. Configuring my home network to allow SSH access from my personal PC to each device in the CML Lab which Netmiko relies on.




