for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="  ")
    print("  ")

print("****************************************************************************************")

for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end="  ")
    print("")

print("****************************************************************************************")

for i in range(65,70,1):
    for j in range(65,i+1):
        print(chr(j),end="")
    print("")