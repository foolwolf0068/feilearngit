'''
小甲鱼视频 24
'''

def hanoi(n, x = 'X', y = 'Y', z = 'Z'):

    if n == 1:
        print(x, '-->', z)
    else:
        #
        hanoi(n-1, x, z, y) # 将前 n-1 个盘子从x移动到y 上
        print(x, '-->', z)  # 将最后一个从x 移动到 z 上
        hanoi(n-1, y, x, z) # 将y 上的n-1个盘子从y移到z上

n = int(input('请输入汉诺塔的层数：'))

hanoi(n, 'A', 'B', 'C')
