import math
n=int(input("Enter number of ingredients: "))
items={"name":[],"price":[]}
sauce=[0,0,0]; sauceN=0
totalN=0; totalF=0;totalS=0
for i in range(n):
    items["name"].append(input("Enter name of item:(Include main in the name if ingreident is main item) "))
    n=int(input("Enter the number of that item required: "))
    if n==1:
        pass
    else:
        n=n-math.ceil(n*43.5/100)
    items["price"].append(int(input("Enter price of item: "))*n)
sauceN=int(input("Enter how many sauce needed: "))
sauceN=sauceN-math.ceil(sauceN*43.5/100)
check=input("do you have items which do not have return rate? Y/N: ")
check=check.lower()
if check=='yes' or check=='y':
    items["name"].append(input("Enter the name: "))
    n=int(input("Enter how many needed: "))
    items["price"].append(int(input("Enter the price: "))*n)
for i in range(3):
    sauce[i]=int(input("Enter the price of sauces: normal, fancy, spec: "))
print(items,"sauce required of prices nomral, fancy, special: ", sauce)
for i in range(len(items["price"])):
    if 'main' in items['name'][i]:
        pass
    else:
        totalN+=items['price'][i]
Total=totalN
totalS=totalN+sauceN*sauce[2]
totalF=totalN+sauceN*sauce[1]
totalN=totalN+sauceN*sauce[0]
check=input("is the item 10 piece? Y/N: ")
check=check.lower()
TaxFee=2800;ItemValue=int(input("Enter the item value: "))
usageFee=((ItemValue * 0.1125)*TaxFee)/100
if check=='y' or check=='yes':
    n=10
    print("for whole batch: \n")
    print("price for each batch is \n normal sauce:",totalN+usageFee )
    print("for fancy", totalF+usageFee )
    print("for spec", totalS+usageFee)
    print("without sauce: ", Total+usageFee)
    print("\nfor each in batch: \n")
else:
    n=1
print("price for normal sauce:",totalN/n+usageFee/10 )
print("for fancy", totalF/n+usageFee/10 )
print("for spec", totalS/n+usageFee/10)
print("without sauce: ", Total/10+usageFee/10)