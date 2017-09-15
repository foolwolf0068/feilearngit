'''
FishC C23-24
'''
# 0
def binNew(n):

    list1 = ''
    while True:
        q = n // 2
        list1 = str(n % 2) + list1
        if q == 0 :
            return list1
        
        n = q

print(binNew(7))

def binNew1(n):
    if (n // 2) :
        return binNew1(n // 2) + str(n % 2)
    else:
        return '1' if (n % 2) else '0'
'''
        if (n % 2) :
            return '1'
        else:
            return '0'
'''
print(binNew1(10))

# 1
def get_digits(n):
    return get_digits(n // 10) + [n % 10] if (n // 10) else [n % 10]
'''
    if (n//10) :
        return get_digits(n // 10) + [n % 10] if (n // 10) else [n % 10]
    else:
        return [n % 10]
'''

print(get_digits(123125))

# 2

def isHwf(str2):
    
    if len(str2) >= 2 and str2[0] == str2[-1]:
        return isHwf(str2[1:-2])

    elif len(str2) >= 2 and str2[0] != str2[-1]:
        return False
    else:
        return True
    
def main(str1):
    if isHwf(str1):
        print('%s 是回文字符串' % str1)
    else:
        print('%s 不是回文字符串' % str1)

main("h")


# 3

def getYear(n):
    if n < 1 and str(n).isdigit():
        print('输入有误，n必须为正整数！！！')
        return 10
        
    return getYear(n-1) + 2 if n != 1 else 10




print(getYear(5))
