# Rupesh Dharme
# 31124
# TE 01
# L1
# Assignment 09

# Write a program for DNS lookup. Given an IP address as input, it should return URL and 
# vice-versa.

import dns.resolver as resolver

if __name__ == '__main__':
    with open('prompt.txt', 'r') as f:
        prompt = f.read()
    while True:
        choice = int(input(prompt).strip())
        if choice == 1:
            domain = input('Enter the domain: ').strip()
            result = resolver.resolve(domain, "A")
            print(f'IP Address corrosponding to the domain is/are: ')
            for i in result:
                print(str(i))
            print()
        elif choice == 2:
            ip = input('Enter an IP Address: ').strip()
            try:
                result = resolver.resolve_address(ip)
                print(f'Domain name corrosponding to the ip address is/are: ')
                for i in result:
                    print(i)
                print()
            except:
                print('ERROR Retreiving information.')
            
        elif choice == 3:
            print(f'Thank you')
            break
        else:
            print(f'Invalid choice. Try again.')