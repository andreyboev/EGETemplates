"""
# Решение I
ip = '255.255.248.0'
print(2 ** ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]).count('0') - 2)
"""

from ipaddress import ip_network
net = ip_network("0.0.0.0/255.255.248.0")
print(net.num_addresses - 2)
