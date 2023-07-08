UserNumber = int(0)
FibonacciNumber = int(0)

def GenerateFibonacci(Number: int):
    Fibonaccis = list()
    FibonacciOfNumber = int()

    Fibonaccis.append(0)
    Fibonaccis.append(1)
    for Counter in range(0, Number, 1):
        if Counter > 1:
            Fibonaccis.append((Fibonaccis[(Counter - 1)] + Fibonaccis[(Counter - 2)]))

    if (Number == 0):
        FibonacciOfNumber = Fibonaccis[0]
    elif (Number == 1):
        FibonacciOfNumber = Fibonaccis[1]
    else:
        FibonacciOfNumber = (Fibonaccis[(Number - 1)] + Fibonaccis[(Number - 2)]) 

    return FibonacciOfNumber

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