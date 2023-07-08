UserNumber = int(0)
FibonacciNumber = int(0)

def GenerateFibonacci(Number: int):
    if (Number == 0):
        return 0
    elif (Number == 1):
        return 1
    else:
        return (GenerateFibonacci(Number - 1) + GenerateFibonacci(Number - 2))

while (True):
    try:
        UserNumber = int(input("Please Enter Your Number : "))
        if (UserNumber < 0):
            print('\a' + "Error: Your Number Have To Be Bigger Than Zero.")
            continue
        else:
            break
    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

FibonacciNumber = GenerateFibonacci(UserNumber)

print(f"Fibonacci Of Your Number Is {FibonacciNumber}")