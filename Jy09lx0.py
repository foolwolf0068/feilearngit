'''
Fish C c9ex0
'''

# 0

count = 3
while (True and count >0):
    code = input("Please enter your password:")
    if "*" in code:
        print("The password doesn't include '*'!", end = "")
        if count == 1 :
            print("You have %d time to enter!"% count, end = "")
        else:
            print("You have %d times to enter!"% count, end = "")
        continue
    elif code =='feige':
        print('Correct, logging...')
        break
    else:
        print("The password is wrong!",end = "")
    count -= 1
    if count == 1 :
        print("You have %d time to enter!" % count, end = "")
    else:
        print("You have %d times to enter!"% count, end = "")
        
# 1        
def isSxh(x):    
    str1 = str(x)
    if not str1.isdigit():
        print("The number must be an int number!!!")
        return False
    num = int(str1[0])**3 + int(str1[1])**3 + int(str1[2])**3
    return (True if num == x else False)
for i in range(100,1000):
    if isSxh(i):
        print(i)
        
# 2
for i in range(0,4):
    for j in range(0,4):
        for k in range(6,-1,-1):
            if i + j + k == 8:
                print("R"*i, end = "")
                print("Y"*j, end = "")
                print("B"*k)

                
    
