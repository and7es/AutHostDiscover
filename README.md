# AutHostDiscover
This script allows you to perform a ping sweep using nmap. It is possible to configure the mask from / 24 onwards and it goes through all the staggered hosts of the third octet.

**Usage**:

```
python AutHostDiscover.py -h                     
usage: AutHostDiscover.py [-h] -i IPRANGE [-e IFACE] -m MASK [-o]

options:
  -h, --help            show this help message and exit
  -i IPRANGE, --IpRange IPRANGE
                        IP Range
  -e IFACE, --iface IFACE
                        Network Interface. Ex -e tun0
  -m MASK, --mask MASK  Subnet mask, between 24 - 32
  -o, --output          Save each result in a separate file

Example: python AutHostDiscover.py -i 172.16.0.0 -m 24
```
