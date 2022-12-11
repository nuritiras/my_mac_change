import re
import subprocess
import optparse


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()


def change_mac_address(interface, mac_address):
    subprocess.call(["ip", "link", "set", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", mac_address])
    subprocess.call(["ip", "link", "set", interface, "up"])


def control_new_mac(interface):
    ip_address_show = subprocess.check_output(["ip", "address", "show", "dev", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ip_address_show))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


print("MAC Changer Started")
(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface, user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
    print("Success!!!")
else:
    print("Error!!!")
