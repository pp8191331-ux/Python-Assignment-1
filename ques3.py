#John is trying to solve the arithmetic series(AP).He wants to find two things in the series
# 1. He wants to find nth terms in the series
# 2. He wants to find the sum up to the nth term.
a = [2, 5, 8, 11, 14, 17, 20]
sum = 0
APlenght = len(a)
for i in range(0,APlenght):
     if a[i] == a[APlenght-1]:
        print("nth term is: ", a[i])

for i in range(0,APlenght):
    sum = sum + a[i]

print("Sum of Arithmetic series is: ", sum)