ip = input("Enter an IP address: ")
mask = int(ip[-2:])
ip = ip[:-3]
print('IP:', ip,'Mask:', mask)
iplist = []
for i in ip.split('.'):
    iplist.append(f'{int(i) :08b}')
ipbin = '.'.join(iplist)
print('IP:',ipbin)
subnet = ''
c = 1
for i in range(1, 33):
    if c<= mask:
        subnet+='1'
    else:
        subnet+='0'
    if c%8==0 and c!=32:
        subnet+='.'
    c+=1
print('Subnet:', subnet)
iplist = subnet.split('.')
iplist = [int(i, 2) for i in iplist]
subnet = '.'.join(map(str, iplist))
print('Subnet:', subnet)
range = 2**(32-mask)
print(range)
print(ipbin)
ipbin = ipbin.replace('.', '')
print(ipbin)
lower = ipbin[:mask] + '0'*(32 - mask)
upper = ipbin[:mask] + '1'*(32 - mask)
print(lower, upper)
lower = '.'.join(str(int(i, 2)) for i in [lower[0: 8], lower[8:16], lower[16:24], lower[24:32]])
upper = '.'.join(str(int(i, 2)) for i in [upper[0: 8], upper[8:16], upper[16:24], upper[24:32]])
print(lower, upper)