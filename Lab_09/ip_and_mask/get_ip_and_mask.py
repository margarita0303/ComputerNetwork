import netifaces

for interface in netifaces.interfaces():
    try:
        print(f'Interface: {interface}')
        print(f"IP Address: {netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']}")
        print(f"Mask: {netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']}")
    except:
        pass
