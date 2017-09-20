'''FishC 33'''
try:
    
    f = open('test.txt','a')
    print(f.write('wrong is wrong!!!'))
    sum = 1 + '1'
    

    
except OSError as reason:
    print('The file is wrong !!! \nThe reason is %s' % str(reason))
except TypeError as reason:
    print('The type is wrong !!! \nThe reason is %s' % str(reason))

finally:
    f.close()
