'''
FishC C30
'''
import os

def fileStatistics(path_name):
    # path_name = "********"
    flag = 1
    expandname=[]
    #count = []
    for root, dirs, files in os.walk(path_name):
        if flag == 1:
            flag = 2 # just show in the 1st dir
            # print(root)
            # print(files)
            dir_number = len(dirs)
            #print(len(dirs))
            #print(dirs)
            
            for file in files:
                # print(file)
                name = os.path.splitext(file)
                if (name[1]) and (len(name[1])<6):
                    expandname.append(name[1])
    nameset = list(set(expandname))
    for i in nameset:
        print('The number of [%s] in this dictionary is %d'\
              %(i, expandname.count(i)))

    print('The number of [%s] in this dictionary is %d'%('wenjianjia', dir_number))
    # print(nameset)

def main():
    path_name = input("Please enter your absolute path:\n") #"feilearngit"
    fileStatistics(path_name)

if __name__ == '__main__':
    main()
