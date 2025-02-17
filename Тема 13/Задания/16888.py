"""
# Решение I (наполовину ручной способ)
ip = '98.162.71.94'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
print()
ip = '98.162.71.64'
print(' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')]))
"""

from ipaddress import ip_network
count = 2**32
for mask in range(33):
    net = ip_network(f'98.162.71.94/{mask}', False)
    if str(net.network_address) == '98.162.71.64':
        count = min(count, net.num_addresses)
print(count)
