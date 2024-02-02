x = input('How much money do you have?  ')
x = int(x)
print('You have ', x, ' dollars')
while True:
    r = input('Reset your money? Yes/No  ')
    if r=='Yes': 
        x = input('How much money do you have?  ')
        x = int(x)
        print('You have ', x, ' dollars')
    else: break

while True:
    buf = input('\nAdd an expense or income record with description and amount:\n')
    usr = buf.split( )
    if len(usr)<2:
        print('Re-enter the record')
        continue
    mon = int(usr[0])
    obj = usr[1]
    if mon<0:
        s = 'You spent {:d} dollars on {:s}'
        print(s.format(-mon, obj))
    elif mon>0:
        s = 'You earned {:d} dollars from {:s}'
        print(s.format(mon, obj))
    x = x+mon
    print('Now you have ', x, ' dollars')

