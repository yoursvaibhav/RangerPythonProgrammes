row=int(input("Enter rows "))
for i in range(row):
    for j in range(row):
        if(i+j) >= row-1:
            print("*",end='')
        else:
            print(" ",end='')
    print("*" * i)
    print()