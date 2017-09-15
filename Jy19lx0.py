'''
FishC C19lx
'''

#0
def isHwl(str1):
    
    a = len(str1)
    if a == 1:
        return True
    b = a // 2
    i = 0
    while i <= b:
        if str1[i] != str1[a-1-i]:
            return False
        i += 1

    return True

def main():
    str1 = input('请输入一句话：')
    if isHwl(str1):
        print('是回文联！')
    else:
        print('不是回文联！')
main()

# 1
def count(*str1):
    a = len(str1)
    for each in range(a):
        count = [0] * 4
        for i in str1[each]:
            if i.isalpha():
                count[0] += 1

            elif i.isdigit():
                count[1] += 1
            elif i.isspace():
                count[2] += 1
            else:
                count[3] += 1
        print('第 %d 个字符串共有：'% (each+1), end = "")
        print('英文字母 %d 个，'% (count[0]), end = "")
        print('数字 %d 个，'% (count[1]), end = "")
        print('空格 %d 个，'% (count[2]), end = "")
        print('英其他字符 %d 个。'% (count[3]))

def main():
    count("I love fishc.com","I love you, you love me.")

main()


                
