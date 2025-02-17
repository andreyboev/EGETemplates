from ipaddress import ip_network

max_m = 0
for m in range(33):
    net1 = ip_network(f'98.162.71.150/{m}', False)
    net2 = ip_network(f'98.162.71.140/{m}', False)
    if net1 == net2:
        max_m = max(max_m, m)
print(max_m)
