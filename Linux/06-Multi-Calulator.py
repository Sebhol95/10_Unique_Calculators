# Created by Sebhol95 for repository "Calculators" https://github.com/Sebhol95/Calculators

x = 1
print ("\n")
print ("The Simple Subtract, add, multiply and divide Calculator")
print ("")
x = int(input("Press 1 to calculate or 0 to exit "))
print ("")
while (x > 0):

    def subtract(x, y):
       return x - y

    def add(x, y):
       return x + y

    def multiply(x, y):
       return x * y

    def divide(x, y):
       return x / y

    print("")
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4):")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
       print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
       print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
       print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
       print(num1,"/",num2,"=", divide(num1,num2))
    else:
       print("Invalid input")
