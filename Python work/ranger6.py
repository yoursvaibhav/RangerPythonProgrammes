unit=float(input("Enter the units consumed "))
if unit <= 50:
    cost= unit * 0.50
    print("cost for ",unit," unit  is ",cost)
elif unit <=150:
    cost= unit * 0.75
    print("cost for ",unit," unit  is ",cost)
elif unit <=250:
    cost= unit * 1.20
    print("cost for ",unit," unit  is ",cost)
else:
    cost= unit * 1.50
    print("cost for ",unit," unit  is ",cost)


