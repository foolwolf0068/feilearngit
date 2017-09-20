# -*- coding: utf-8 -*-
'''
FishC C30 lx3
'''
import os

def VedioStatistics(path_name):
    
    video_expandname = ['.rmvb', '.avi', '.mp4', '.flv']
    file_address = []
    flag = 1
    for root, dirs, files in os.walk(path_name):
        if flag == 1:                       
            for file in files:
                # print(file)
                name = os.path.splitext(file)
                if (name[1].lower() in video_expandname) and (name[1]):
                    file_found = os.path.join(root, file)
                    # print(file_found)
                    file_address.append(file_found)
    return file_address

def Vedioname_save(filename, address):
    f = open(filename, 'w')
    for i in address:
        f.write(i+"\n")
    f.close()    
    

def main():
    path_name = input("Please enter your absolute path:\n") #"feilearngit
    filename = 'videolist.txt'
    address =VedioStatistics(path_name)
    Vedioname_save(filename, address)
    

if __name__ == '__main__':
    main()
