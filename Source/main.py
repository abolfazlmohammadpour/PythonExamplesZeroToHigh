UserNumber = int(0)

while (True):
    try:
        UserNumber = int(input("Please Enter Your Number : "))
        break
    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

if ((UserNumber % 2) == 0):
    print("Your Number Is Even")
else:
    print("Your Number Is Odd")