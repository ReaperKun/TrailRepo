import math
def return_rate(n):
    return n-(math.ceil(((n*43.5)/100)))
def price_calculator(price,n):
    return price*n
def fee_calci(ItemValue,TaxFee):
    return ((ItemValue * 0.1125)*TaxFee)/100

items={"name":["corn","pumpkin","potatoes","ghoul yarrow","elusive","firetouch mullein","t8 raw","t7 raw","t6 raw","t6 milk","t8 milk","goose eggs","flour",'bread'],
       "price":[399,396,416,400,470,507,483,470,464,420,397,396,440,404]}
sauce=[2720,9610,25663]
ava_energy=3476
TaxFee=2800

#pork pie
total=items["price"][items['name'].index('corn')]*return_rate(18)+items["price"][items['name'].index('flour')]*return_rate(36)+items["price"][items['name'].index('t7 raw')]*return_rate(72)+items["price"][items['name'].index('t6 milk')]*return_rate(18)
ItemValue=576
usage_fee=fee_calci(ItemValue,TaxFee)*10
print("for pork pie: \n")
print("price is: ", (total/10)+usage_fee/10,"with usage fee per batch is:", total+usage_fee)
print("price is: ", (total+sauce[0]*return_rate(90))/10+usage_fee/10,"with usage fee per batch is:", (total+sauce[0]*return_rate(90))+usage_fee)
print("price is: ", (total+sauce[1]*return_rate(90))/10+usage_fee/10,"with usage fee per batch is:", (total+sauce[1]*return_rate(90))+usage_fee)
print("price is: ", (total+sauce[2]*return_rate(90))/10+usage_fee/10,"with usage fee per batch is:", (total+sauce[2]*return_rate(90))+usage_fee)
#ava beef
ItemValue=1152
usage_fee=fee_calci(ItemValue,TaxFee)*10
name=''
for i in range(4):
    if i==0:
        name='corn'
        total+=price_calculator(items["price"][items['name'].index(name)],return_rate(36))
    elif i==1:
        name='pumpkin'
        total+=price_calculator(items["price"][items['name'].index(name)],return_rate(36))
    elif i==2:
        name='t8 raw'
        total+=price_calculator(items["price"][items['name'].index(name)],return_rate(72))
    else:
        total+=price_calculator(ava_energy,90)
print("for ava beef: \n")
print("price is: ", total/10+usage_fee/10,"with usage fee per batch is:", total+usage_fee)
for i in range(3):
    print("price is: ", (total+price_calculator(sauce[i],return_rate(90)))/10+usage_fee/10,"with usage fee per batch is:", (total+price_calculator(sauce[i],return_rate(90)))+usage_fee)
#ava pork
#deadwater
#beef stew
#pork ome
#dusthole
#puremist
#kraken