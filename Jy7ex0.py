'''
Fish C C7-8
'''
# 0
import re
condition = re.compile(r'^[-+]?[0-9]+\.?[0-9]*$')

grade = input("Please enter a score number:")
result = condition.match(grade)

if not result:
    print("The score you entered is not valid!")
else:
    n = eval(grade)
    if 100 >= n >= 90:
        print("A")
    elif 80 <= n < 90:
        print("B")
    elif 60 <= n < 80:
        print("C")
    elif 0 <= n < 60:
        print("D")
    else:
        print("The score you entered is not valid!")

# 1
x, y, z = 4, 6, 2
small = x if (x < y and x < z) else ( y if y < z else z)
print(small)
