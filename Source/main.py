UserWeight = float(0)
UserHeight = float(0)
UserBMI = float(0)

while (True):
    try:
        UserWeight = float(input("Please Enter Your Weight : "))
        break
    except ValueError:
        print('\a' + "Error: Please Just Enter A Number.")
        continue

while (True):
    try:
        UserHeight = float(input("Please Enter Your Height : "))
        break
    except:
        print('\a' + "Error: Please Enter Just A Number.")
        continue

UserBMI = ((UserWeight / (UserHeight ** 2)) * 10000)
print(f"Your BMI Is : {UserBMI}")