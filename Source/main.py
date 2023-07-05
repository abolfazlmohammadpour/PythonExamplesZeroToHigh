Sum = int(1)
Subtraction = int(2)
Multiplication = int(3)
Division = int(4)

NumberOne = float(0)
NumberTwo = float(0)
Operation = int(0)

# Getting NumberOne Value From User
while (True):
    try:
        NumberOne = float(input("Please Enter Number One : "))
        break

    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

# Getting NumberTwo Value From User
while (True):
    try:
        NumberTwo = float(input("Please Enter Number Two : "))
        break

    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

# Getting Operation Value From User
while (True):
    try:
        print(str(Sum) + ") Sum")
        print(str(Subtraction) + ") Subtraction")
        print(str(Multiplication) + ") Multiplication")
        print(str(Division) + ") Division")
        Operation = int(input("Please Enter Number Of An Operation : "))

        if (Operation >= Sum) and (Operation <= Division):
            break
        else:
            print('\a' + "Error: Please Enter A Valid Operation")
            continue

    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

# Calculate The Operation And Print Result To User
match (int(Operation)):
    case (1):
        SumIs = float((NumberOne + NumberTwo))
        print("Sum Is : " + str(SumIs))

    case (2):
        SubtractionIs = float((NumberOne - NumberTwo))
        print("Subtraction Is : " + str(SubtractionIs))

    case (3):
        MultiplicationIs = float((NumberOne * NumberTwo))
        print("Multiplication Is : " + str(MultiplicationIs))

    case (4):
        try:
            DivisionIs = float((NumberOne / NumberTwo))
            print("Division Is : " + str(DivisionIs))
        except ZeroDivisionError:
            print('\a' + "Error: You Can Not Divide To Zero.")
