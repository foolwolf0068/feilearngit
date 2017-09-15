'''
FishC C15
'''
while True:
    num = input("Please enter an int number(enter 'Q' or 'q' for quit):")
    if num.lower() == 'q':
        break
    print('Decimal -> Hex : {0} -> {1}'.format(int(num), hex(int(num))))
    print('Decimal -> Oct : {0} -> {1}'.format(int(num), oct(int(num))))
    print('Decimal -> Bin : {0} -> {1}'.format(int(num), bin(int(num))))
    
