from random import randint, seed
from time import time

CapitalAlphabetic = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
SmallAlphabetic = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
SpecialCharacters = ('@', '_')
Numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

CapitalAlphabeticLength = int(len(CapitalAlphabetic))
SmallAlphabeticLength = int(len(SmallAlphabetic))
SpecialCharactersLength = int(len(SpecialCharacters))
NumbersLength = int(len(Numbers))

UserRequest = str()
UserPassword = list()
UserRandomNumber = int()

while True:
    UserRequest = str(input("Would You Like To Generate A Password?(Yes/No):"))

    if ((UserRequest == "Yes") or (UserRequest == "No")):
        break
    else:
        print('\a' + "Error: Invalid Input, The Input Have To Be Yes Or No.")
        continue

if (UserRequest == "Yes"):
    while True:
        try:
            UserRandomNumber = int(input("Please Enter A Random Number For Generating Password : "))
            break
        except ValueError:
            print('\a' + "Error: Please Just Enter A Number.")
            continue
else:
    exit()

seed((int(time()) / UserRandomNumber))

for Counter in range(0, 32, 4):
    UserPassword.append(CapitalAlphabetic[randint(0, (CapitalAlphabeticLength - 1))])
    UserPassword.append(SmallAlphabetic[randint(0, (SmallAlphabeticLength - 1))])
    UserPassword.append(SpecialCharacters[randint(0, (SpecialCharactersLength - 1))])
    UserPassword.append(Numbers[randint(0, (NumbersLength - 1))])

TemperatureOfConverting = str()
for Counter in range(0, 32):
    TemperatureOfConverting += UserPassword[Counter]

UserPassword = TemperatureOfConverting

print("Your Password Is :", UserPassword)
