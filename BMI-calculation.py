"""Write a Python program to calculate body mass index."""
wgt_unit = input("YOU WILL ENTER YOUR WEIGHT IN 'kg' OR 'lbs'? ")
wgt_unit = wgt_unit.lower()
weight = int(input("ENTER YOUR WEIGHT: "))
hgt_unit = input("YOU WILL ENTER YOUR HEIGHT IN 'm' OR 'in'? ")
hgt_unit = hgt_unit.lower()
height = int(input("ENTER YOUR HEIGHT: "))
i wgt_unit == "kg" and hgt_unit == "metres":
    BMI = weight/(height**2)
    print(f'YOUR BMI IS: {BMI}')
eli wgt_unit == "lbs" and hgt_unit == "in":
    BMI = (703 * weight) / (height**2)
    print(f'YOUR BMI IS: {BMI}')

i BMI < 18.5:
    print("YOU ARE UNDERWEIGHT")
eli BMI >= 18.5 and BMI < 24.9:
    print("YOU ARE NORMAL")
eli BMI >= 25 and BMI < 29.9:
    print("YOU ARE OVERWEIGHT")
else:
    print("YOU ARE OBESE")
#just add "f", I have removed 2 "f" from "if" and 3 from "elif".
