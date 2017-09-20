'''
FishC C37 # 0
'''
class Ticket:
    def __init__(self, price = 100): # construct function
        self.price = price
        self.vocation = 'no'
        
    def getPrice(self):
        com1 = input('Please confirm vocation or not?(yes or no) ')
        if com1.lower() not in 'no':
            self.price_adult = self.price * 1.2
            self.price_child = self.price_adult * 0.5
            print('The price for adult is %f and for child is %f on holiday.'\
                  % (self.price_adult, self.price_child))
            self.vocation = 'yes'
        else:
            self.price_adult = self.price
            self.price_child = self.price_adult * 0.5
            print('The price for adult is %f and for child is %f on holiday.'\
                  % (self.price_adult, self.price_child))
            self.vocation = 'no'  


    def getTotal(self):
        print('please enter the number of adults and the number of child:')
        adult = eval(input('Adult: '))
        child = eval(input('Children: '))
        return adult * self.price_adult + child * self.price_child
        
        
        
        
    
