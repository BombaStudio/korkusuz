import subprocess

def changer(interface, mac):
	print("[Gaster]mac changer started")
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac])
	subprocess.call(["ifconfig",interface,"up"])
