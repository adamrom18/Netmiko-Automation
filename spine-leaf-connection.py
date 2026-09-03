from netmiko import ConnectHandler

# ----------------------------------------
# Device Inventory
# ----------------------------------------

inventory = {
    "iol-l2-Spine1": {
        "ip_addr": "10.0.0.2",
        "username": "cisco",
        "password": "cisco",
        "device_type": "cisco_xe",
    },
    "iol-l2-Spine2": {
        "ip_addr": "10.0.0.3",
        "username": "cisco",
        "password": "cisco",
        "device_type": "cisco_xe",
    },
    "iol-Leaf1": {
        "ip_addr": "10.0.0.254",
        "username": "cisco",
        "password": "cisco",
        "device_type": "cisco_xe",
    },
    "iol-Leaf2": {
        "ip_addr": "10.0.0.253",
        "username": "cisco",
        "password": "cisco",
        "device_type": "cisco_xe",
    }
}

# ----------------------------------------
# Interface Change Info
# ----------------------------------------

ip_info = {
    "iol-l2-Spine1": {
        "Ethernet0/1": {
            "ip": "10.0.1.1",
            "mask": "255.255.255.252",
        },
        "Ethernet0/2": {
            "ip": "10.0.1.13",
            "mask": "255.255.255.252",
        },
        "Loopback01": {
            "ip": "172.20.0.1",
            "mask": "255.255.255.0",
        }
    },
    "iol-l2-Spine2": {
        "Ethernet0/1": {
            "ip": "10.0.1.5",
            "mask": "255.255.255.252",
        },
        "Ethernet0/2": {
            "ip": "10.0.1.9",
            "mask": "255.255.255.252",
        },
        "Loopback02": {
            "ip": "172.20.0.2",
            "mask": "255.255.255.0",
        }
    },
    "iol-Leaf1": {
        "Ethernet0/1": {
            "ip": "10.0.1.2",
            "mask": "255.255.255.252",
        },
        "Ethernet0/2": {
            "ip": "10.0.1.10",
            "mask": "255.255.255.252",
        },
        "Loopback03": {
            "ip": "172.20.0.3",
            "mask": "255.255.255.0",
        }
    },
    "iol-Leaf2": {
        "Ethernet0/1": {
            "ip": "10.0.1.6",
            "mask": "255.255.255.252",
        },
        "Ethernet0/2": {
            "ip": "10.0.1.14",
            "mask": "255.255.255.252",
        },
        "Loopback04": {
            "ip": "172.20.0.4",
            "mask": "255.255.255.0",
        }
    }
}

# ----------------------------------------
# OSPF Change Info
# ----------------------------------------

ospf_info = {
    "iol-l2-Spine1": {
        "10.0.1.0": "0.0.0.3",
        "10.0.1.12": "0.0.0.3",
    },
    "iol-l2-Spine2": {
        "10.0.1.4": "0.0.0.3",
        "10.0.1.8": "0.0.0.3",
    },
    "iol-Leaf1": {
        "10.0.1.0": "0.0.0.3",
        "10.0.1.8": "0.0.0.3",
        "10.1.10.0": "0.0.0.255",
        "10.1.20.0": "0.0.0.255",
        "10.1.30.0": "0.0.0.255",
    },
    "iol-Leaf2": {
        "10.0.1.4": "0.0.0.3",
        "10.0.1.12": "0.0.0.3",
        "10.2.10.0": "0.0.0.255",
        "10.2.20.0": "0.0.0.255",
        "10.2.30.0": "0.0.0.255",
    }
}

# ----------------------------------------
# Vlan Change Info
# ----------------------------------------

vlan_info = {
    "iol-Leaf1": {
        "10": {
            "ip": "10.1.10.1",
            "mask": "255.255.255.0",
            "name": "0010-PROD-DUB",
        },
        "20": {
            "ip": "10.1.20.1",
            "mask": "255.255.255.0",
            "name": "0020-DEV-DUB",
        },
        "30": {
            "ip": "10.1.30.1",
            "mask": "255.255.255.0",
            "name": "0030-TEST-DUB",
        }
    },
    "iol-Leaf2": {
        "10": {
            "ip": "10.2.10.1",
            "mask": "255.255.255.0",
            "name": "0010-PROD-DUB",
        },
        "20": {
            "ip": "10.2.20.1",
            "mask": "255.255.255.0",
            "name": "0020-DEV-DUB",
        },
        "30": {
            "ip": "10.2.30.1",
            "mask": "255.255.255.0",
            "name": "0030-TEST-DUB",
        }
    }
}

# ----------------------------------------
# Access Port Config
# ----------------------------------------
access_info = {
    "iol-Leaf1" : {
        "Ethernet0/3": {
            "vlan": "10",
        },
        "Ethernet1/0": {
            "vlan": "10",
        },
        "Ethernet1/1": {
            "vlan": "20",
        },
        "Ethernet1/2": {
            "vlan": "30",
        },
        "Ethernet1/3": {
            "vlan": "30",
        }
    },
    "iol-Leaf2" : {
        "Ethernet0/3": {
            "vlan": "10",
        },
        "Ethernet1/0": {
            "vlan": "10",
        },
        "Ethernet1/1": {
            "vlan": "20",
        },
        "Ethernet1/2": {
            "vlan": "30",
        },
        "Ethernet1/3": {
            "vlan": "30",
        }
    },

}

# ----------------------------------------
# Command Templates
# ----------------------------------------

show_run_template = "show run {}"
interface_template = "interface {}"
interface_ip_template = "ip address {} {}"
ospf_ip_template = "network {} {} area 0"

# ========================================
# Main Loop
# ========================================

# Iterating over ip_info dictionary an
for hostname, ip_data in ip_info.items():
    host_ip = inventory[hostname]["ip_addr"] # The hostname is used to obtain the value of ip from inventory variable
    username = inventory[hostname]["username"]  # The hostname is used to obtain the value of username from inventory variable
    password = inventory[hostname]["password"]  # The hostname is used to obtain the value of password from inventory variable
    device_type = inventory[hostname]["device_type"] # The hostname is used to obtain the value of device_type from inventory variable

    # Initiating a connection to the device
    print("Establishing connection with {}".format(hostname))
    device = ConnectHandler(
        host=host_ip,
        username=username,
        password=password,
        device_type=device_type,
    )  

    commands = [] # Holds all config commands

    # ----------------------------------------
    # Interface Config
    # ----------------------------------------
    for interface, details in ip_data.items():
        print("Building interface configuration...")

        interface_command = interface_template.format(interface)
        commands.append(interface_command)

        commands.append("no switchport")

        interface_ip_command = interface_ip_template.format(
            details["ip"],
            details["mask"]
        )
        commands.append(interface_ip_command)

        commands.append("ip ospf network point-to-point")
        commands.append("no shutdown")
        commands.append("exit")

    # ----------------------------------------
    # OSPF Config
    # ----------------------------------------

    print("Building OSPF configuration...")

    commands.append("router ospf 1")

    ospf_data = ospf_info.get(hostname, {})

    for ospf_ip, ospf_mask in ospf_data.items():
        ospf_ip_command = ospf_ip_template.format(
            ospf_ip,
            ospf_mask 
        ) 
        commands.append(ospf_ip_command)

    commands.append("exit")

    # ----------------------------------------
    # Vlan Config
    # ----------------------------------------

    print("Building Vlan configuration...")

    vlan_data = vlan_info.get(hostname, {})

    for vlan_id, vlan_details in vlan_data.items():

        #Creating Vlan
        commands.append("vlan {}".format(vlan_id))
        commands.append("name {}". format(vlan_details["name"]))
        commands.append("exit")

        #Creating SVI
        commands.append("interface vlan {}".format(vlan_id))

        vlan_ip_command = interface_ip_template.format(
            vlan_details["ip"],
            vlan_details["mask"]
        )
        commands.append(vlan_ip_command)
        commands.append("no shutdown")
        commands.append("exit")

    # ----------------------------------------
    # Access Port Config
    # ----------------------------------------

    print("Building Access Port configuration...")

    access_data = access_info.get(hostname, {})

    for interface_access, vlan_access in access_data.items():

        access_interface = interface_template.format(interface_access)
        commands.append(access_interface)

        commands.append("switchport mode access")
        commands.append(
            "switchport access vlan {}".format(
                vlan_access["vlan"]
            )
        )
        commands.append("no shutdown")
        commands.append("exit")


    # ----------------------------------------
    # Apply Config
    # ----------------------------------------

    print(commands) # print the commands and make sure the format is correct
    print("Applying the configuration")
    device.send_config_set(commands) # Applies config to device

    # ----------------------------------------
    # Validate Config
    # ----------------------------------------

    print("Validating if the configuration was successfully applied...")
    show_command = show_run_template.format(commands[0])
    show_run_output = device.send_command(show_command)
    print(show_run_output)

    ospf_output = device.send_command( 
        "show running-config | section router ospf"
    )
    print(ospf_output)

    vlan_output = device.send_command(
        "show vlan brief"
    )
    print(vlan_output)

    svi_output = device.send_command(
        "show ip interface brief | include Vlan"
    )
    print(svi_output)

    # ----------------------------------------
    # Disconnect
    # ----------------------------------------

    print("Disconnecting from the {} ".format(hostname))
    device.disconnect()
    print("==================================================")

    
