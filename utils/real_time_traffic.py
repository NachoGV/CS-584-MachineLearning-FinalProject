# Using scapy, this script will sniff the network for packets and print out the source and destination IP addresses
# as well as the protocol and length of the packet. This script will also print out the source and destination MAC
# addresses for each packet.

from scapy.all import *

total = 0
mario = 0
no_ip = 0

def print_pkt(pkt):
    global total
    global mario
    global no_ip
    
    total = total + 1

    try:
        print('Source IP: ' + pkt[IP].src)
        if pkt[IP].src == '192.168.43.221':
            mario = mario + 1
    except:
        no_ip = no_ip + 1
        pass

    print(total)

if __name__ == '__main__':
    pkt = sniff(prn=print_pkt, count = 1000)
    wrpcap('../inputs/sniffed.pcap', pkt)

    print('Total packets: ', total)
    print('Mario packets: ', mario)
    print('No IP packets: ', no_ip)