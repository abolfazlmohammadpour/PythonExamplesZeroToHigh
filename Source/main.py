Number = int(0)
FactorilOfNumber = int(0)

def GenerateFactorial(Number: int):
    if Number <= 0:
        return 1
    else:
        return (Number * GenerateFactorial((Number - 1)))



while (True):
    try:
        Number = int(input("Please Enter Your Number : "))
        break
    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

FactorilOfNumber = GenerateFactorial(Number)

print(f"Factorial Of Your Number Is {FactorilOfNumber}")

