    
def currency_converter(num):

    Penny =  0
    Nickle = 0
    Dime = 0
    Quart = 0
    One = 0
    Five = 0
    Ten = 0
    Fifty = 0
    hundo = 0
    
    while num >= 100:
        num -= 100
        hundo += 1

    while num >= 50:
        num -=50
        Fifty += 1

    while num >= 10:
        num -=10
        Ten += 1

    while num >= 5:
        num -= 5
        Five += 1

    while num >= 1:
        num -= 1
        One += 1

    while num >= 0.25:
        num -= 0.25
        Quart += 1

    while num >= 0.1:
        num -= 0.1
        Dime += 1

    while num >= 0.05:
        num -= 0.05
        Nickle += 1

    while num >= 0:
        num -= 0.01
        Penny += 1

    print(str(hundo) + " Hundreds")
    print(str(Fifty) + " Fifties")
    print(str(Ten) + " Tens")
    print(str(Five) + " Fives")
    print(str(One) + " Ones")
    print(str(Quart) + " Quarters")
    print(str(Dime) + " Dimes")
    print(str(Nickle) + " Nickles")
    print(str(Penny) + " Pennies")
    
num = float(input("What amount of cash would you like converted?"))
currency_converter(num)
            
    