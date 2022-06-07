#Write a C program to print sum of digits enter by user
a=int(input("Enter any number "))
sum=0
while a>0:
    b = a % 10
    sum+=b
    a=a//10
print(sum)
