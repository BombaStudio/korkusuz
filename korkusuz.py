import modules.mac_changer as mac_changer
import modules.net_scaner as scaner
import modules.builder as builder
import subprocess
import optparse
from os import *

def bc():
	x = input("")
	if x == "ex" or x == "exit":
		console()
def t(c):
	if c == "hello Gaster":
		print("hello user")
	if c == "mac_changer":
		interface = input("interface:")
		mac = input("mac:")
		mac_changer.changer(interface, mac)
	if c == "net_scaner":
		arp = input("exeample:\n	[ip]/[24 / 16 / 8 default: 24]\nrange:")
		mac = input("exeample:\n	[default: ff:ff:ff:ff:ff:ff]\nmac:")
		net_scaner(arp, mac)
	if c == "ex" or c == "exit":
		exit()
	else:
		system(c)
def console():
	while True:
		c = input("<GaStEr>__>")
		t(c)

if __name__ == '__main__':
	console()
