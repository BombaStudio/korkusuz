import scapy.all as scapy

def scaner(ipfield, mac):
	apr_req_pac = scapy.ARP(pdst=ipfield)
	braodcast_pack = scapy.Ether(dst=mac)
	combined_pack = broadcast_pack / arp_req_pack
	(answered_list, unanswered_list) = scapy.srp(combined_pack, timeout = 1)
	answered_list.summary()
