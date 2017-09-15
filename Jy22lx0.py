'''
FishC C22
'''

# 0
def power(x,y):
    if not str(y).isdigit():
        print('y must be an int number!!!')
        return None
    elif y == 1:
        return x
    else:
        return x * power(x,y-1)


print(power(2,5))

# 1
def gcd(x,y):

    if y > x:
        x, y = y, x    
    r = x % y

    if r == 0:
        return y
    else:
        return gcd(y,r)

print(gcd(6,46))
    
'''
# 小甲鱼的程序
def gcd(x, y):
    if y:
        return gcd(y, x % y)
    else:
        return x
    
print(gcd(4, 6))
'''
