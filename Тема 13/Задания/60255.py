"""
count = 0
for i in range(256 - 240):
    ip = f'192.168.32.{160 + i}'
    s = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])
    if s.count('1') % 2 == 0:
        count += 1
print(count)
"""


from ipaddress import ip_network
count = 0
net = ip_network(f'192.168.32.160/255.255.255.240', False)
for ip in net:
    if f'{ip:b}'.count('1') % 2 == 0:
        count += 1
print(count)