class Person:
    def __init__(self,name):
        self.name = name
    
    def printstring(self):
        h = self.name
        
        print(h.upper())

y=str(input())

x=Person(y)

x.printstring()