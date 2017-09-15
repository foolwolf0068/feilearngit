'''
Fish C C4lx
'''
# 0
from random import randint
print("---------------Ready, Go!---------------")
a = randint(1, 10) # yield a int number between 1 and 10
count = 1
while count <= 3:
    print("The %d guess:" % count)
    temp = input("Please enter an integer number:")
    guess = eval(temp)
    if guess == a:
        print("Oh, you know me?!")
        print("But...., no reward!")
        break
    elif guess >a :
        print("The number you guessed is a litter bigger than my number! Please try again...")
    else:
        print("The number you guessed is a litter smaller than my number! Please try again...")
    if guess != a and count == 3:
        print("You have no chance to guess the 4th time.")
    count += 1    
print("------------Game over!!!------------")

# 1
num1 = int(input("Please enter an integer:"))
for i in range(1, num1+1):
    print(i)

# 2
num2 = int(input("Please enter an integer:"))
for i in range(num2, 0, -1):
    print(" " * i, end = "")
    print("*" * i)
    
