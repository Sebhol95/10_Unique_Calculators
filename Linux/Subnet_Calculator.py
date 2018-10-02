# Created by Sebhol95 for repository "Calculators" https://github.com/Sebhol95/Calculators

x = 1
print("")
x = int(input("Press 1 to calculate a new subnett or 0 to exit "))
while (x > 0):
    print ("")
    Subnet = int(input ("How many host do you need in your network: "))
    print ("")
    if Subnet <=2 :
        print ("You can use a /30 network that has 4 addresses and 1 host - network mask is 255.255.255.252")
    elif Subnet <=6:
        print ("You can use a /29 network that has 8 addresses and 6 hosts - network mask is 255.255.255.248")
    elif Subnet <=14:
        print ("You can use a /28 network that has 16 addresses and 14 hosts - network mask is 255.255.255.240")
    elif Subnet <=30:
        print ("You can use a /27 network that has 32 addresses and 30 hosts - network mask is 255.255.255.224")
    elif Subnet <=62:
        print ("You can use a /26 network that has 64 addresses and 62 hosts - network mask is 255.255.255.192")
    elif Subnet <=126:
        print ("You can use a /25 network that has 128 addresses and 126 hosts - network mask is 255.255.255.128")
    elif Subnet <=254:
        print ("You can use a /24 network that has 256 addresses and 254 hosts - network mask is 255.255.255.0")
    elif Subnet <=510:
        print ("You can use a /23 network that has 512 addresses and 510 hosts - network mask is 255.255.254.0")
    elif Subnet <=1022:
        print ("You can use a /22 network that has 1024 addresses and 1022 hosts - network mask is 255.255.252.0")
    elif Subnet <=2046:
        print ("You can use a /21 network that has 2048 addresses and 2046 hosts - network mask is 255.255.248.0")
    elif Subnet <=4094:
        print ("You can use a /20 network that has 4096 addresses and 4094 hosts - network mask is 255.255.240.0")
    elif Subnet <=8190:
        print ("You can use a /19 network that has 8192 addresses and 8190 hosts - network mask is 255.255.224.0")
    elif Subnet <=16382:
        print ("You can use a /18 network that has 16384 addresses and 16382 hosts - network mask is 255.255.192.0")
    elif Subnet <=32766:
        print ("You can use a /17 network that has 32768 addresses and 32768 hosts - network mask is 255.255.192.0")
    elif Subnet >=32766:
        print ("Stop lying, you dont need such a big subnet :) ") 
