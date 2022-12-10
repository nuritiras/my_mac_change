import subprocess
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")
    return parse_object.parse_args()

def change_mac_address(interface,mac_address):
    subprocess.call(["ip", "link", "set", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", mac_address])
    subprocess.call(["ip", "link", "set", interface, "up"])

print("MAC Changer Started")
(user_input,arguments)=get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)