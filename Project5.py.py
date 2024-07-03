import random 


port_to_protocol = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    80: "HTTP",
    110: "POP3",
    137: "NetBIOS",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

def identifyProtocolFromPort():
    port = random.choice(list(port_to_protocol.keys()))
    protocol = port_to_protocol[port]
    print(f"Option 1: Identify the port's PROTOCOL.")
    print("----------------------------------------")
    answer = input(f"What is the protocol for port {port} (m=Main Menu)?  ").strip().upper()
    if answer == "M":
        return
    elif answer == protocol:
        print("Correct answer!\n")
    else:
        print(f"Incorrect. The correct answer is {protocol}.\n")
    identifyProtocolFromPort()


def identifyPortFromProtocol():
    protocol = random.choice(list(port_to_protocol.values()))
    ports = [port for port, proto in port_to_protocol.items() if proto == protocol]
    port = random.choice(ports)
    print(f"Option 2: Identify the port's NUMBER.")
    print("----------------------------------------")
    answer = input(f"What is the number for protocol {protocol} (m=Main Menu)?  ").strip().upper()
    if answer == "M":
        return
    elif answer == str(port):
        print("Correct answer!\n")
    else:
        print(f"Incorrect. The correct answer is {port}.\n")
    identifyPortFromProtocol()


def mainMenu():
    print("Main Menu:")
    print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
    print("2. Given a port protocol, identify a port NUMBER.")
    print("3. Exit\n")
    
    while True:
        choice = input("Choice: ").strip()
        
        if choice == "1":
            identifyProtocolFromPort()
        elif choice == "2":
            identifyPortFromProtocol()
        elif choice == "3":
            print("\nProgram Complete. I hope this has helped in studying for the CompTIA A+ certification.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    mainMenu()
