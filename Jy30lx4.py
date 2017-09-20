'''
FishC C30 lx4
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

def word_find(fileaddress, word):
    f = open(fileaddress)    
    str1s = f.readlines()
    f.close()    
    line_index = 0
    linelist= []
    positon_index = []
    for str1 in str1s:
        line_index += 1
        if word in str1:
            linelist.append(line_index)
            positon_index.append(word_index(str1,word))    
    return linelist, positon_index      
            
            
def word_index(str1,word):
    num_index = []
    if word in str1:
        num = str1.count(word)
        index1 = str1.find(word)
        num_index.append(index1 + 1)
        for i in range(1,num):
            index1 = str1.find(word,index1) + 1
            num_index.append(str1.find(word,index1) + 1)
            # index1 = str1.find(word,index1)
    return num_index

def main():
    path_name = input("Please enter the original dictionary:")
    file_name = input("please enter the file name you search:")
    word = input('Please enter the keyword you want to search:')
    print_command = input("Do you want to print the specific position of ['%s'] (YES/NO):" % word)
    fileaddresses = file_find(path_name,file_name)
    for fileaddress in fileaddresses:
        (lines, positions) = word_find(fileaddress, word)        
        if print_command.lower() in 'yes':
            print('=' * 80)
            print("The keywords '%s'are found in [%s]"%(word,fileaddress))
            for i in range(len(lines)):                
                print('The keyword are found in '+str(lines[i])+'line, and the position is '+str(positions[i]))
                

if __name__ == '__main__':
    main()
