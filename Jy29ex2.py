'''
FishC C29ex1
'''

def save_file(boy,girl,count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()
   
def split_file(filename):
    
    f = open(filename)

    boy = []
    girl = []
    count = 1
    for each in f:
        if each[:6] != '======' :
            (role,line_spoken) = each.split(':',1)
            if role =="小甲鱼":
                boy.append(line_spoken)
            if role == "小客服":
                girl.append(line_spoken)
                
        else:
            save_file(boy,girl,count)
            '''
            file_name_boy = 'boy_' + str(count) + '.txt'
            file_name_girl = 'girl_' + str(count) + '.txt'

            boy_file = open(file_name_boy,'w')
            girl_file = open(file_name_girl,'w')

            boy_file.writelines(boy)
            girl_file.writelines(girl)

            boy_file.close()
            girl_file.close()
            '''

            boy = []
            girl = []
            count += 1

    save_file(boy,girl,count)
    '''        
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy,'w')
    girl_file = open(file_name_girl,'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()
    '''        
split_file('record.txt')
