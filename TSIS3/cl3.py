class shape:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        h=self.length*self.width
        print(h)

    def initial(self):
        print("area=0")

class rectangle(shape):
    def __init__(self,length,width):
        super().__init__(length,width)



x=rectangle(2,7)
x.area()
