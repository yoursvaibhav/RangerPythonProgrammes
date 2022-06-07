sal=float(input("Enter the basic salary "))
if sal <=10000:
    hra=sal * (20/100)
    da=sal * (80/100)
    total= sal + hra+ da
    print("Gross salary is ",total)
elif sal <=20000:
    hra=sal * (25/100)
    da=sal * (90/100)
    total= sal + hra+ da
    print("Gross salary is ",total)
else:
    hra = sal * (30 / 100)
    da = sal * (95 / 100)
    total = sal + hra + da
    print("Gross salary is ", total)