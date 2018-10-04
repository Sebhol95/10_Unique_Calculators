# Created by Sebhol95 for repository "Calculators" https://github.com/Sebhol95/Calculators

x = 1
print ("\n")
print ("Exponent Calculator")
print ("")
x = int(input("Press 1 to calculate or 0 to exit "))
while (x > 0):
    print("")
    print ("The exponent Calculator")
    
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter raised to power number 2: "))
    numex = (num1, num2)
    exp = (num1 ** num2)
              
    print ("Number 1 to the power of number 2 is =", exp)
