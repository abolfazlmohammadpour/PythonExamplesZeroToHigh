Number = int(0)
FactorilOfNumber = int(0)

def GenerateFactorial(Number: int):
    FactorilOfNumber = int(1)

    for Counter in range(1, (Number + 1), 1):
        FactorilOfNumber = (FactorilOfNumber * Counter)

    return FactorilOfNumber



while (True):
    try:
        Number = int(input("Please Enter Your Number : "))
        break
    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

FactorilOfNumber = GenerateFactorial(Number)

print(f"Factorial Of Your Number Is {FactorilOfNumber}")

