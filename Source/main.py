from random import randint as Random

UserNumber = int(0)
GeneratedNumber = int(0)

def GenerateRandomNumber():
    return int(Random(0, 9))

while (True):
    try:
        UserNumber = int(input("Please Guess A Number (The Number Have To Be From 0 To 9) : "))

        if ((UserNumber <= 9) and (UserNumber >= 0)):
            break
        else:
            print('\a' + "Error: The Number Have To Be From 0 To 9.")
            continue

    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

GeneratedNumber = GenerateRandomNumber()

if (GeneratedNumber == UserNumber):
    print("You Are A Winner")
else:
    print("You Are A Losser")