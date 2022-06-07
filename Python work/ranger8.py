b=int(input("Enter the DAA marks out of 100 "))
c=int(input("Enter the DLDM marks out of 100 "))
d=int(input("Enter the OS marks out of 100 "))
e=int(input("Enter the M4 marks out of 100 "))
f=int(input("Enter the BHR marks out of 100 "))

total=b+c+d+e+f
percentage = (total/500)*100

if percentage >= 90:
    print("You got ",round(percentage),"% and your Grade is A")
elif percentage >=80:
    print("You got ",percentage,"% and your Grade is B")
elif percentage >=70:
    print("You got ",percentage,"% and your Grade is C")
elif percentage >=60:
    print("You got ",percentage,"% and your Grade is D")
elif percentage >=40:
    print("You got ",percentage,"% and your Grade is E")
else:
    print("You got ",percentage,"% and your Grade is F")