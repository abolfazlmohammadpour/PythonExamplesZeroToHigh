Number = int(0)
IsPrime = bool(True)

while True:
    try:
        Number = int(input("Please Enter Your Number : "))
        if (Number > 0):
            break
        else:
            print('\a' + "Error: Your Number Have To Be Bigger Than Zero.")
            continue
    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

for Counter in range(2, Number):
    if ((Number % Counter) == 0):
        IsPrime = False
        break

if IsPrime:
    print("Your Number Is A Prime Number")
else:
    print("Your Number Is Not A Prime Number")