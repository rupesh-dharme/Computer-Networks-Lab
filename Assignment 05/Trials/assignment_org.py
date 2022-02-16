def splitIp(ip):
    mask = int(ip[-2:])
    ip = ip[:-3]
    return ip, mask

def decToBin(ip):
    return '.'.join(f'{int(i):08b}' for i in ip.split('.'))

def binToDec(ip):
    return '.'.join(f'{int(i, 2)}' for i in ip.split('.'))

def lowerUpper():
    ip = ipbin.replace('.', '')
    lower = ip[:mask] + '0'*(32 - mask)
    upper = ip[:mask] + '1'*(32 - mask)
    lower = '.'.join(str(int(i, 2)) for i in [lower[0: 8], lower[8:16], lower[16:24], lower[24:32]])
    upper = '.'.join(str(int(i, 2)) for i in [upper[0: 8], upper[8:16], upper[16:24], upper[24:32]])
    l = int(lower.split('.')[-1])
    u = int(upper.split('.')[-1])
    r = (l + u)//2
    random = '.'.join(i for i in lower.split('.')[:-1]+[str(r)])
    return lower, random, upper

def findSubnet(mask):
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
    return subnet

def present():
    print(f'\nIP address:            {ip} ({ipbin})\n')
    print(f'Mask is:               {mask}\n')
    print(f'Subnet decimal is:     {subnetdec} ({subnet})\n')
    print(f'Pingable IPs:          {lower} to {upper}\n')
    print(f'Random Pingable IPs:   {random}\n')

if __name__ == '__main__':

    ip, mask = splitIp(input("\nEnter an IP address:   "))
    ipbin = decToBin(ip)
    subnet = findSubnet(mask)
    subnetdec = binToDec(subnet)
    lower,random, upper = lowerUpper()
    present()