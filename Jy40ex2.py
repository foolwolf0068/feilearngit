'''
FishC  Jy 40
'''

class C:
    def __init__(self, x = 0):
        self.x = x



def main():
    c1 = C()
    # hasattr(object, name)
    print(hasattr(c1, 'x'))
    
    # getattr(object, name[,default])
    print(getattr(c1,'x'))
    # print(getattr(c1,'y'))
    print(getattr(c1,'y','The objext has not a attribute"y"!'))
    
    # setattr(object, name, value)
    print(setattr(c1,'y',"feige"))
    print(hasattr(c1,'y'))

    # delattr(pbject, name)
    print(delattr(c1,'y'))
    
    

    



if __name__ == "__main__":
    main()
