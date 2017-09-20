'''
FishC  Jy 40
'''

class C:
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size = value
    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize) # set a seted property!!!



def main():
    c1 = C()
    print(c1.getSize())
    print(c1.x)
    c1.x = 18
    print("c1.x = 18")
    print(c1.x)
    print(c1.size)
    print(c1.getSize())
    print("del c1.x")
    del c1.x
    print(c1.size)
    
    
if __name__ == "__main__":
    main()
