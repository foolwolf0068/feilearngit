'''
FishC C36 # 1
'''

class Rectangle:
    length = 5.00
    width = 4.00

    def setRect(self):
        print('Please enter the length and width of the Rectangle...')
        self.length = eval(input('Length:'))
        self.width = eval(input('Width:'))
    def getRect(self):
        print("The Rectangle's length and width is %.2f and %.2f respectively."\
              %(self.length,self.width))
    def getArea(self):
        return self.length * self.width


    
