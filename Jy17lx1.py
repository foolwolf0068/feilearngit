'''
FishC C17-18
'''

def MyFirstFunction(name):
    'Define a parameter---name'
    # name is just a parameter
    print('argument is transfering into the function' + name)
# 0
def MyListSum(list,base = 3):
    print(sum(list) * base)

# 1
def Sxh():
    for i in range(100,1000):
        str1 = str(i)
        if i == (int(str1[0]) ** 3 + int(str1[1]) ** 3 + int(str1[2]) ** 3) :
            print(i)
Sxh()

# 2
def findstr():
    str1 = input("Please enter the target string:")
    str2 = input("Please enter the sub string(two chars):")
    a = str1.count(str2)
    if a <= 1 :
        print("The sub happens %d time in the target string." % a)
    else:
        print("The sub happens %d times in the target string." % a)

findstr()
