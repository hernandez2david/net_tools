import scapy.all as scapy
import  optparse

def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="ip_range", help="Enter the ip Range that will be scanned")
    (options, arguments) = parser.parse_args()
    if not options.ip_range:
        parser.error("[+] Please specify a The range of IPs")
    else:
        return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ethernet_frame = broadcast/arp_request
    answered = scapy.srp(ethernet_frame,timeout = 1, verbose = False)[0]
    client_list = []
    for element in answered:
        client_dict = {"ip" : element[1].hwsrc, "mac" : element[1].psrc}
        client_list.append(client_dict)

    return client_list
    

def print_scanned(client_list):
    print("IP\t\t\t\t\tMAC\n" + ("="*60))
    for client in client_list:
        print(client["ip"]+"\t\t\t"+client["mac"])

options = arguments()
dictionaries_captured = scan(options.ip_range)
print_scanned(dictionaries_captured)


