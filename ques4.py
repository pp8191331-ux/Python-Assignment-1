#Write a program that converts and prints user given measurement in inches into
#1. foot(12 inches)
#2. yard(36 inches)
#3. centimeters(2.54 inches)
#4. meters(39.37 inches)

input = int(input("Enter value in inches: "))
foot = input/12
yard = input/36
centimeters = input*2.54
meter = input/39.37

print(f"{input} in foot are {foot}\n")
print(f"{input} in yard are {yard}\n")
print(f"{input} in centimeter are {centimeters}\n")
print(f"{input} in meter are {meter}\n")
