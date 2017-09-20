'''
FishC C30 lx1
'''
import os
def file_find(path_name,file_name):
    file_address = []
    for root, dirs, files in os.walk(path_name):
        for file in files:
            if file_name == file:
                file_found = os.path.join(root, file)
                # print(file_found)
                file_address.append(file_found)

    return file_address

def main():
    path_name = input("Please enter the original dictionary:")
    file_name = input("please enter the file name you search:")
    fileaddress = file_find(path_name,file_name)
    for i in fileaddress:
        print(i)

if __name__ == '__main__':
    main()

    
    
                
        
