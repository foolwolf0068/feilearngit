'''
Fish C C5lx
'''
# 0
from random import randint
print("---------------Ready, Go!---------------")
a = randint(1, 10) # yield a int number between 1 and 10
count = 1
times = 3
while count <= times:
    temp = input("Please enter an integer number:")
    while (not temp.isdigit()):       
        print("The %d guess:" % count)
        print("You input is not valid!")        
        count += 1
        if count > times:
            print("Oops,You have no chance to guess the 4th time.")
            break
        temp = input("Please enter an integer number:")
              
    if temp.isdigit() and eval(temp) == a:
        print("Oh, you know me?!")
        print("But...., no reward!")
        break
    elif temp.isdigit() and eval(temp) >a :
        print("The number you guessed is a litter bigger than my number! Please try again...")
    elif temp.isdigit() and eval(temp) <a :
        print("The number you guessed is a litter smaller than my number! Please try again...")
    if temp.isdigit() and eval(temp) != a and count >= times:
        print("Oops,You have no chance to guess the 4th time.")
    count += 1
    
print("------------Game over!!!------------")

# 1

year = input("Please enter a year:")
if not year.isdigit():
    print("Your input is not valid, please input a year number!")
else:
    a = eval(year)
    if (a % 400 ==0) or ((a % 4 ==0)and (a % 100 !=0)):
        print("The %d year is a leap year!" % a)
    else:
        print("The %d year is not a leap year!" % a)
