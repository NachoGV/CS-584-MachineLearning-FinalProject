# Using scapy, this script will sniff the network for packets and print out the source and destination IP addresses
# as well as the protocol and length of the packet. This script will also print out the source and destination MAC
# addresses for each packet.

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(prn=print_pkt, count=1)
wrpcap('sniffed.pcap', pkt)

