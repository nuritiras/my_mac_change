import subprocess

print("MAC Changer başladı")
subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether","00:11:22:22:11:11"])
subprocess.call(["ifconfig","eth0","up"])