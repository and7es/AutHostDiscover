#!/usr/bin/env python

import sys
import os
import argparse
import ipaddress

#Menú
parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -i 172.16.0.0 -m 24\r\n")
parser.add_argument('-i', '--IpRange', help="IP Range", required=True)
parser.add_argument('-e', '--iface', help="Network Interface. Ex -e tun0")
parser.add_argument('-m', '--mask', help="Subnet mask, between 24 - 32", required=True)
parser.add_argument('-o', '--output', help="Save each result in a separate file", action="store_true")
args = parser.parse_args()


ip_list = args.IpRange.split('.') 

oct2=int(ip_list[2])

while oct2 <256:
	subnet = ip_list[0] + '.' + ip_list[1] + '.' + str(oct2) + '.' + ip_list[3] +'/' + args.mask
	print ('Ping Sweep: ' + subnet)
	file_output = ip_list[0] + '_' + ip_list[1] + '_' + str(oct2) + '_' + ip_list[3] +'.txt'
	if args.iface:
		command1 = 'nmap -sn -e ' + args.iface + ' ' + subnet + ' -v -oG temp.txt'
	else:
		command1 = 'nmap -sn ' + subnet + ' -v -oG temp.txt'

	if args.output:
		command2 = "cat temp.txt | awk '/Up$/{print $2}' | tee " + file_output
	else:
		command2 = "cat temp.txt | awk '/Up$/{print $2}'"

	result1 = os.popen(command1).read()
	result2 = os.system(command2)
	oct2+=1
