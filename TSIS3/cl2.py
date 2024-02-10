class shape:
    def __init__(self,length,width):
        self.length=length
        self.width=width


    class square:
        def __init__(self,length):
            self.length = length
        
        def area(self):
            g=self.length**2
            print(g)
        
        def initial(self):
            print("area=0")
    
    def area(self):
        h=self.length*self.width
        print(h)

    def initial(self):
        print("area=0")


x=shape(2,3)

x.initial()
