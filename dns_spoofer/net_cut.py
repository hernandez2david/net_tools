#! usr/bin/env/python
from scapy.all import *
from netfilterqueue import NetfilterQueue

def process_packet(packet):
    print(packet)

nfqueue = NetfilterQueue()
nfqueue.bind(0, process_packet)
nfqueue.run()
