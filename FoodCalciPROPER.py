import math

items=[438,401,530,434,442,473,481,425,449,363,372,270,505,482,494,477,442]
#["corn"0,"pumpkin"1,"potatoes"2,"ghoul yarrow"3,"elusive"4,"firetouch mullein"5,"t8 raw"6,"t7 raw"7,"t6 raw"8,"t6 milk"9,"t8 milk"10,"goose eggs"11,"flour"12,'bread'13,'t8 butter'14,'t6 butter'15,'foxglove'16]

itemsT8=[64988,9328]
#[deadwatereel0,thunderfallLurch11]

itemsT7=[25000,8497,72500]
#[Dusthole0,frostpeak1, puremist2]

itemst6=[79000,4898,4778]
#Kraken0,redspring1,rushwater2

sauce=[0,4689,13900,39000]
ava_energy=2400
TaxFee=499

#last to first

item_valueT8=[750,1152,576,750,1080,504]

item_valueT7=[750,576,750,576,750,1080,504]

item_valueT6=[260,384,192,260,360,168,750,576]

Selling_Tax=6.5

def return_rate(n):
    return n-(math.ceil(((n*43.5)/100)))

def price_calculator(price,n):
    return price*return_rate(n)

def fee_calci(ItemValue):
    return (((ItemValue * 0.1125)*TaxFee)/100)

def itemsall(itemcount,prices,v):
    total=0
    flag=False
    for i in range(len(itemcount)):
        if itemcount[i]>10 and flag==False:
            flag=True
        total+=price_calculator(itemcount[i],prices[i])
    if flag==True:
        return total+ (fee_calci(v)*10)
    else: 
        return total+fee_calci(v)



print("----------------T8 ALL--------------")
    
print("\nDead water eel")
for i in sauce:
    print(itemsall([27,1,6,6,6],[i,itemsT8[0],items[1],items[3],items[10]],item_valueT8[0]))
    
print("\nAvalonian Beef Stew")
for i in sauce:
    print(itemsall([90,36,72,90],[i,items[1],items[6],ava_energy],item_valueT8[1])/10)
    
print("\nBeef Stew")
for i in sauce:
    print(itemsall([90,36,72],[i,items[1],items[6]],item_valueT8[2])/10)
    
print("\nThunderFall lurcher sandwhich")
for i in sauce:
    print(itemsall([27,1,6,6,6],[i,itemsT8[1],items[1],items[3],items[14]],item_valueT8[3]))
    
print("\nAvalonian beef sandwhich")
for i in sauce:
    print(itemsall([90,36,72,18,90],[i,items[13],items[6],items[14],ava_energy],item_valueT8[4])/10)

print("\n beef sandwhich")
for i in sauce:
    print(itemsall([90,36,72,18],[i,items[13],items[6],items[14]],item_valueT8[5])/10)
    
print("-------------T7 ALL-------------")

print("\n puremist snapper")
for i in sauce:
    print(itemsall([27,1,6,6,6],[i,itemsT7[2],items[0],items[5],items[10]],item_valueT7[0]))
    
print("\nRoasted pork")
for i in sauce:
    print(itemsall([90,72,36,36],[i,items[7],items[0],items[10]],item_valueT7[1])/10)
    
print("\nDeadeye pie")
for i in sauce:
    print(itemsall([27,1,6,6,6],[i,itemsT7[1],items[0],items[5],items[7]],item_valueT7[2]))
 

print("Pork pie")
for i in sauce:
    print((itemsall([90,18,36,72,18],[i,items[0],items[12],items[7],items[9]],item_valueT7[3]))/10)

   
print("\ndusthole")
for i in sauce:
    print(itemsall([278,1,6,6,6],[i,itemsT7[0],items[0],items[5],items[7]],item_valueT7[4]))

print("\nAvalonian pork ome")
for i in sauce:
    print(itemsall([90,36,72,18,90],[i,items[10],items[7],items[11],ava_energy],item_valueT7[5])/10) 
   
print("\nPork ome")
for i in sauce:
    print(itemsall([90,36,72,18],[i,items[0],items[7],items[11]],item_valueT7[6])/10)
    
print("-------------T6 foods----------------")

print("\nRed spring eel")
for i in sauce:
    print(itemsall([9,1,2,2,2],[i,itemst6[1],items[2],items[16],items[9]],item_valueT6[0]))
    
print("\nKraken salad")
for i in sauce:
    print(itemsall([27,1,6,6,6],[i,itemst6[0],items[2],items[16],items[8]],item_valueT6[6]))