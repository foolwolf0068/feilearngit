'''
FishC C10lx
'''
# 0
# method 1
member1 = ['xioajiayu', 'heiye','mitu','yijing', 'qiuwuxieyang' ]
member2 = [88, 90, 85, 90, 88]
for i in range(1,10,2):
    member1.insert(i,member2[int((i-1)/2)])
member = member1[:]
print(member)

# method 2
member1 = ['xioajiayu', 'heiye','mitu','yijing', 'qiuwuxieyang' ]
member2 = [88, 90, 85, 90, 88]
member0 = []
for i in range(len(member2)):
    member0.append(member1[i])
    member0.append(member2[i])

member = member0[:]
print(member)

# 1
for i in member:
    print(i)

# 2
for i in range(len(member)):
    print(member[i], end = " ")
    if i % 2 == 1:
        print()
