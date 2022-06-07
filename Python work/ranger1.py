a = int(input("Enter any number "))
original = a
temp = 0
while a > 0:
    temp = temp + (a % 10) * (a % 10) * (a % 10)
    a = a // 10
if original == temp:
    print("Armstrong number")
else:
    print("not Armstrong number")
