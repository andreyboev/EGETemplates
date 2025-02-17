count = 0
for i3 in range(256 - 248):
    for i4 in range(256):
        ip = f'172.16.{168 + i3}.{i4}'
        s = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])
        if s.count('1') % 5 != 0:
            count += 1
print(count)

# С библиотекой
from ipaddress import ip_network
count = 0
net = ip_network(f'172.16.168.0/255.255.248.0', False)
for ip in net:
    if f'{ip:b}'.count('1') % 5 != 0:
        count += 1
print(count)