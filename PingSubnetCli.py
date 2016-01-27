# /usr/lib/python2.7/site-packages/CliPlugin/

import BasicCli
import CliParser
import netaddr
import time
import os

tokenPing = CliParser.KeywordRule('pingsubnet', helpdesc='Send echo messages to a cidr address')


def doPing(network):
    livecounter = 0
    offlinecounter = 0
    cidr = netaddr.IPNetwork(network)
    print("-----------------------------------------")
    print("Date\t\t" + time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Timezone\t" + time.strftime("%Z"))
    print("-----------------------------------------")
    for ip in cidr:
        if ip != cidr.network and ip != cidr.broadcast:     # Only hosts in CIDR
            response = os.system("ping -c 2 -w1 " + str(ip) + " > /dev/null 2>&1")
            if response == 0:
                print ip, "up"
                livecounter += 1
            else:
                print ip, "down"
                offlinecounter +=1
    print("-----------------------------------------")
    print("CIDR\t\t" + str(cidr))
    print("Network ID\t" + str(cidr.network))
    print("Broadcast\t" + str(cidr.broadcast))
    print("Total Hosts\t" + str(cidr.size - 2))
    print("-----------------------------------------")
    print("Hosts Online\t" + str(livecounter))
    print("Hosts Online\t" + str(offlinecounter))


def getNetworks(mode):
    i = 0
    results = ['172.16.1.4/28', '192.168.99.2/30', '172.16.0.1/32']
    print("-----------------------------------------")
    print("Network\t\tSubnet")
    print("-----------------------------------------")
    for result in results:
        print(str(i) + "\t\t" + results[i])
        i += 1
    var = raw_input("\nEnter the network to ping (0-" + str(len(results) - 1) + "): ")
    doPing(results[int(var)])


BasicCli.EnableMode.addCommand((tokenPing, getNetworks))
