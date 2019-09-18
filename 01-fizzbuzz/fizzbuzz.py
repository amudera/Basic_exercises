
def fizz(num):
    for num in range(num):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num%3 == 0:
            print("fizz")
        elif num%5 == 0:
            print("buzz")
        else:
            print(num)

fizz(50)

