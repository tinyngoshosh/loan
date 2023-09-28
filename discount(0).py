#code to calculate discount on purchase
amount=float(input("enter the amount:"))
if amount>=1000:
    discount=0.05*amount
    print("the discount",discount)
else:
    print("no discount")
    