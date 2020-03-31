#! usr/bin/env/python
from netfilterqueue import NetfilterQueue
import scapy.all as scapy

def print_and_accept(pkt):
    scapy_packet = scapy.IP(pkt.get_payload())
    print (scapy_packet.show())
    pkt.drop()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print
