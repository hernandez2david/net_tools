import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ethernet_frame = broadcast/arp_request
    answered,unanswered = scapy.srp(ethernet_frame,timeout = 1)
    answered.show()

    # arp_request.show()
    #print(ethernet_frame.summary())
    #ethernet_frame.show()
    #scapy.ls(scapy.Ether())
    #print("=" * 60)
    #print(broadcast.summary())
    #print("=" * 60)
    #scapy.ls(scapy.ARP)
    #print("=" * 60)
    #print(arp_request.summary())
    #print(arp_request.summary())
    #arp_request.show()


ip_range = "192.168.1.1/24"

scan(ip_range)
