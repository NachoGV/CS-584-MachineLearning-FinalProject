# Using scapy, this script will sniff the network for packets and print out the source and destination IP addresses
# as well as the protocol and length of the packet. This script will also print out the source and destination MAC
# addresses for each packet.

from scapy.all import *

def print_pkt(pkt):
    print("Source IP: " + pkt[IP].src)
    print("Destination IP: " + pkt[IP].dst)
    print("Protocol: " + pkt[IP].proto)
    print("Length: " + pkt[IP].len)
    print("Source MAC: " + pkt[Ether].src)
    print("Destination MAC: " + pkt[Ether].dst)
    
while True:
    pkt = sniff(prn=print_pkt)