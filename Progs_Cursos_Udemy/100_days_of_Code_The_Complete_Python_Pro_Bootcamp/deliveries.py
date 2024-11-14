print('Welcome to Python Mercado Livre!')
type = input('Which type of delivery do you want? F, N or L: ')
extra_safety = input('Do you want extra protection to your package? y or n:')
bill = 0
if type == 'F':
    bill = 13
    if extra_safety == 'y':
        bill += 5
elif type == 'N':
    bill = 8
    if extra_safety == 'y':
        bill += 5
elif type == 'L':
    bill = 5
    if extra_safety == 'y':
        bill += 5
else:
    print('Invalid option. Please choose F, N or L.')       
print(f'The total cost for your delivery is: R$ {bill}')