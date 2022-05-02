import re

if __name__ == '__main__': 
    with open('addresses.txt') as f:
        addresses = f.read()
#print(addresses) 

pattern = re.compile(r'[a-zA-ZæøåÆØÅ,.]+') # change [\w ] to dot if specialchars are allowed
for line in addresses.split('\n'):
    if pattern.match(line):
        print(pattern.match(line).group())
       