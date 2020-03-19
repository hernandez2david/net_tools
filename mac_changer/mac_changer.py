#! usr/bin/env/python

import subprocess
import optparse
import re


def change_mac(new_mac, interface):
    print("Changing mac address to " + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


def arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Select the interface to change it's MAC address")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="Select the value for the new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.new_mac:
        parser.error("[+] Please specify a MAC Address")
    elif not options.interface:
        parser.error("[+] Please specify an interface")
    else:
        return options


def current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    ifconfig_new_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if ifconfig_new_mac_address:
        return ifconfig_new_mac_address.group(0)
    else:
        print("[+]mac address could not be changed")


options = arguments()

change_mac(options.new_mac, options.interface)


if options.new_mac == current_mac(options.interface):
    print("The new Mac has been changed to "+str(current_mac(options.interface)))


# print ifconfig_result

# Comments from the first version

# ifconfig interface down
# ifconfig interface hw ehter new_interface
# ifconfig interface up

# subprocess.call("ifconfig "+device+" down", shell = "TRUE")
# subprocess.call("ifconfig "+device+" hw ether "+new_mac, shell = "TRUE")
# subprocess.call("ifconfig "+device+" up", shell = "TRUE")
