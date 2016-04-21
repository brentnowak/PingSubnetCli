#!/usr/bin/env bash
cp /mnt/flash/PingSubnetCli.py /usr/lib/python2.7/site-packages/CliPlugin/
chmod 644 /usr/lib/python2.7/site-packages/CliPlugin/PingSubnetCli.py
cd /mnt/flash/netaddr-0.7.18
sudo python setup.py install
