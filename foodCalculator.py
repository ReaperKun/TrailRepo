import math
check='N';i=0;Total=0;n=0
price=[0,0,0]; return_rate=43.5
ingredients={"Name":[],"price":[]}
while check=='N' or check=='NO':
    ingredients["Name"].append(input("enter the {} Ingredient name: ".format(i+1)))
    for j in range(3):
        price[j]=int(input("Enter the {} price: ".format(j+1)))
    else:
        n=int(input("How many of {} needed: ".format(ingredients['Name'][i])))
        if n==1:
            ingredients["price"].append(((price[0]+price[1]+price[2])/3))
        else:
            ingredients["price"].append(((price[0]+price[1]+price[2])/3)*(n-(math.ceil(((n*return_rate)/100)))))
    check=input("Are you done? Y/N: ")
    check=check.upper()
    i+=1
print(ingredients)
making_cost=int(input("Enter making cost: "))
for j in range(len(ingredients["price"])):
    Total+=ingredients['price'][j]
    
print("The Total Cost of Making is: ",Total+making_cost)
selling_price=int(input("Enter the selling price: "))
if selling_price>Total+making_cost:
    print("The profits are ", selling_price-Total+making_cost)
else:
    print("The loss is: ", Total+making_cost-selling_price)