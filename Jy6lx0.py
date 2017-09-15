'''
Fish C C6lx0

'''

# 0
# method 1
print(list(range(1,100,2)))
# method 2
for i in range(100):
    if i % 2 != 0:
        print(i)

# method 3
n = 1
while n:    
    if n > 100:
        break
    print(n)
    n += 2

# 1

# 999999999 ** 99999999999

n = 7
while n:
    if n % 7 == 0 and n % 6 == 5 and n % 5 == 4 and n % 3 == 2 and n % 2 == 1 :
        break
    n += 7

print("The staircase has %d steps!" % n)


    
