
def gcd(x, y):
    
    if x % y:
        return gcd(y, x%y)
    else:
        return y
    
def gcd1(x, y):
    while True:
        r = x % y
        if r == 0 :
            return y        
        x, y = y, r
        
def mingbs(x, y):
    return int(x*y/gcd1(x,y))

# print(gcd1(65,25))


def mingbs1(list1):
    minlb = list1[0]
    for i in list1[1:]:
        minlb = mingbs(minlb,i)
    return minlb

list1 = [2,4,6,15]
print(mingbs1(list1))
        

