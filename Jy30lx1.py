'''
FishC C30 lx1
'''
import os
def file_size_get(path_name):
    # path_name = absolute path
    flag = 1
    file_list=[]
    
    for root, dirs, files in os.walk(path_name):
        if flag == 1:
            flag = 2 # just show in the 1st dir
            for file in files:
                
                file_list.append((file,os.path.getsize(file)))
    return file_list

def main():
    path_name = input("Please enter your absolute path:\n") #"feilearngit"
    file_list = file_size_get(path_name)
    for i in file_list:
        print("%s [%d Bytes]"%(i[0],i[1]))

if __name__ == '__main__':
    main()
