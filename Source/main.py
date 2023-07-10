Number = int(0)
SumOfDivisors = int(0)

while (True):
    try:
        Number = int(input("Please Enter Your Number : "))
        if (Number <= 0):
            print('\a' + "Error: Your Number Have To Be Bigger Than Zero.")
            continue
        else:
            break

    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

for Counter in range(1, Number, 1):
    if (((Number % Counter) == 0)):
        SumOfDivisors += Counter

if ((Number == SumOfDivisors)):
    print("Your Number Is A Perfect Number")
else:
    print("Your Number Is Not A Perfect Number")