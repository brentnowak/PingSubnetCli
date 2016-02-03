# Description

Python script to add a **pingsubnet** command to Arista switches to send echo messages to a CIDR address and print out a report.

# Requirements

EOS 4.14.5 or higher

# Output

```text
switch#pingsubnet
Network         Subnet
0               172.16.1.4/28
1               192.168.99.2/30

Enter the network to ping (0-1): 0
-----------------------------------------
Date            2016-01-27 10:12:10
Timezone        PST
-----------------------------------------
172.16.1.1 up
172.16.1.2 up
172.16.1.3 up
172.16.1.4 up
172.16.1.5 down
172.16.1.6 down
172.16.1.7 down
172.16.1.8 down
172.16.1.9 down
172.16.1.10 up
172.16.1.11 down
172.16.1.12 down
172.16.1.13 down
172.16.1.14 down
-----------------------------------------
CIDR            172.16.1.4/28
Network ID      172.16.1.0
Broadcast       172.16.1.15
Total Hosts     14
-----------------------------------------
Hosts Online    5
Hosts Online    9
```

# Testing

Copy file to /usr/lib/python2.7/site-packages/CliPlugin/

If running EOS version 4.9+, issue **sudo killall FastClid-server** 

# Installation

```text
event-handler Boot-Cli
   trigger on-boot
   action bash sudo /mnt/flash/LoadPingSubnetCli.sh
   delay 60

management api http-commands
   protocol unix-socket
   no shutdown
```

Copy the following files to /mnt/flash
**LoadPingSubnetCli.sh**
**PingSubnetCli.py**
