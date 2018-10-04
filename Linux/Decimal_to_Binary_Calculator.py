# Created by Sebhol95 for repository "Calculators" https://github.com/Sebhol95/Calculators

x = 1
print ("\n")
print ("The Simple addition Calculator")
print ("")
x = int(input("Press 1 to calculate or 0 to exit "))
while (x > 0):
    print ("")
    dec = int(input ("What number do you want to convert? "))
    print ("")
    print("The decimal value of",dec,"is:")
    print(bin(dec),"in binary.")
    print(oct(dec),"in octal.")
    print(hex(dec),"in hexadecimal.")
    print ("")
