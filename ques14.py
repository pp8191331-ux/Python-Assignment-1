#Staircase

m = int(input("Enter number: "))
for i in range(m):
    for j in range(i+1):
      print("#",end = "") #Because print statement carries new lines thats why we are ending it with empty string
    print("\n") 