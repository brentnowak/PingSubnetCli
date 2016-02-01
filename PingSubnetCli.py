# /usr/lib/python2.7/site-packages/CliPlugin/

import BasicCli
import CliParser
import netaddr
import time
import sys
import os

from jsonrpclib import Server

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
            response = doPingHost(ip)
            if response == 0:
                output = str(ip) + " up\n"
                sys.stdout.write(output)
                sys.stdout.flush()
                livecounter += 1
            else:
                output = str(ip) + " down\n"
                sys.stdout.write(output)
                sys.stdout.flush()
                offlinecounter +=1
    print("-----------------------------------------")
    print("CIDR\t\t" + str(cidr))
    print("Network ID\t" + str(cidr.network))
    print("Broadcast\t" + str(cidr.broadcast))
    print("Total Hosts\t" + str(cidr.size - 2))
    print("-----------------------------------------")
    print("Hosts Online\t" + str(livecounter))
    print("Hosts Offline\t" + str(offlinecounter))

def doPingHost(ip):
    response = os.system("ping -c 2 -w1 " + str(ip) + " > /dev/null 2>&1")
    return response

def getNetworks(mode):
    switch = Server("unix:/var/run/command-api.sock")
    result = switch.runCmds(1, ["show ip interface brief"], "text")
    result = result[0]['output']
    result = result.split('\n')

    networks = []

    for row in result:
        row = row.split()
        if len(row) > 0:    # Error check for empty row
            if row[1] != "unassigned":     # Check for assigned networks
                if row[1] != "IP":
                    networks.append(row[1])

    i = 0
    print("-----------------------------------------")
    print("Network\t\tSubnet")
    print("-----------------------------------------")
    for network in networks:
        print(str(i) + "\t\t" + network)
        i += 1
    var = raw_input("\nEnter the network to ping (0-" + str(len(networks) - 1) + "): ")
    doPing(networks[int(var)])


BasicCli.EnableMode.addCommand((tokenPing, getNetworks))
