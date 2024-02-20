# 4)
""" no1, no2 = int(input("Enter no1: ")), int(input("Enter no2: "))
print("No1 is %d, No2 is %d, No1*No2 is %d" %(no1,no2,no1*no2)) """

# 5)
""" tmp_c = float(input("Enter the temperature in Celsius: "))
tmp_f = 32+(tmp_c*(180.0/100.0))
print("Celsius temperature is: %.1f" %tmp_c)
print("Fahrenheit temperature is: %.1f" %tmp_f) """

# leap year
year = int(input("Enter Year: "))
if (year % 400 == 0 and year % 100 == 0):
    print("%d is Leap Year" %year)
elif (year % 4 == 0 and year % 100 != 0):
    print("%d is Leap Year")
else:
    print("%d is Not Leap Year")

