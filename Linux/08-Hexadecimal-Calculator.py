# Created by Sebhol95 for repository "Calculators" https://github.com/Sebhol95/Calculators

x = 1
print ("\n")
print ("The Hexadecimal Calculator")
print ("")
x = int(input("Press 1 to calculate or 0 to exit "))
while (x > 0):
    hex = input ("Enter any number in Hexadecimal form: ")
    if hex == 'x':
        exit()
    else:
        dec = int(hex, 16);
        print (hex, "in Decimal = ", str(dec));
        
