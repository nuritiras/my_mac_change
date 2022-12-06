import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")

(user_input, arguments) = parse_object.parse_args()
interface = user_input.interface
mac_address = user_input.mac_address

print("MAC Changer Started")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])