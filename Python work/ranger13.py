#print the addition of 1st and last digit of number
n=int(input("Enter number "))
a=n%10
while n>9:
    n=n//10
print(a+n)