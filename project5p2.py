





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


protocol_to_port = {v: k for k, v in port_to_protocol.items()}

def main():
    print("Main Menu:")
    print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
    print("2. Given a port protocol, identify a port NUMBER.")
    print("3. Exit")
    
    while True:
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            print("\nProgram Complete. I hope this has helped in studying for the CompTIA A+ certification.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def option1():
    print("\nOption 1: Identify the port's PROTOCOL.")
    print("----------------------------------------")
    
    while True:
        port_number = random.choice(list(port_to_protocol.keys()))
        protocol = port_to_protocol[port_number]
        
        answer = input(f"What is the protocol for port {port_number} (m=Main Menu)? ").strip().upper()
        
        if answer == 'M':
            break
        elif answer == protocol:
            print("Correct answer!\n")
        else:
            print(f"Incorrect. The correct answer is {protocol}.\n")

def option2():
    print("\nOption 2: Identify the port's NUMBER.")
    print("----------------------------------------")
    
    while True:
        protocol = random.choice(list(protocol_to_port.keys()))
        port_number = protocol_to_port[protocol]
        
        answer = input(f"What is the number for protocol {protocol} (m=Main Menu)? ").strip().upper()
        
        if answer == 'M':
            break
        elif answer.isdigit() and int(answer) == port_number:
            print("Correct answer!\n")
        else:
            print(f"Incorrect. The correct answer is {port_number}.\n")

if __name__ == "__main__":
    main()
