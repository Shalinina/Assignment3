inches = float(input("Enter the value of Inches or you can enter a negative value to exit a program"))
while inches > 0:
    cm = inches * 2.54
    print("The converted value in centimeters is" + str(cm))
    break
else:
    print("You entered a negative value: Program ends ")
