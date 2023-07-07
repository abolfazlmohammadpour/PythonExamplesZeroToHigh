UserTemperature = int(0)
ConvertedTemperature = int(0)
Operation = int(0)

while (True):
    print("1) Fahrenheit To Celcius")
    print("2) Celcius To Fahrenheit")

    try:
        Operation = int(input("Please Select A Mode Of Converting : "))
        if ((Operation <= 2) and (Operation >= 1)):
            break
        else:
            print('\a' + "Error: Invalid Operation, Please Try Again.")
            continue
    except ValueError:
        print('\a' + "Error: Please Enter Just A Number.")
        continue

while (True):
    try:
        UserTemperature = int(input("Please Enter Yout Temperature : "))
        break
    except ValueError:
        print('\a' + "Error: Please Enter Just A Number.")
        continue

match (Operation):
    case (1):
        ConvertedTemperature = int((float((UserTemperature - 32)) / 1.8))
        print(f"{UserTemperature}Fahrenheit Degree Is Equal To {ConvertedTemperature}Celcius Degree")
    case (2):
        ConvertedTemperature = int(((float(UserTemperature) * 1.8) + 32))
        print(f"{UserTemperature}Celcius Degree Is Equal To {ConvertedTemperature}Fahrenheit Degree")