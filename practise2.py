price1=float(input('Enter your first price: '))
price2=float(input('Enter your second price: '))
price3=float(input('Enter your third price: '))
name=input('Enter your name: ')

totalBill=price1+price2+price3
averagePrice=(price1+price2+price3)/3

print(f'Total bill amount is {totalBill}')
print(f'Average price is {averagePrice}')

if'S' in name or 's' in name:
    print('S or s is exzist in name.')
else:
    print('NOt have')