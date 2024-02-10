class prime:
    def __init__(self,numbers):
        self.numbers = numbers

    def filter(self):
        for x in self.numbers:
            i = 2
            y=0
            while i < x:
                if x%i==0:
                    y=y+1
                i=i+1
            
            if y<1:
                print(x)
    
    def filterlam(self):
        for x in self.numbers:
            a = 2
            j=0
            while a < x:
                y= lambda a,x : x/a
                if y(a,x)%1==0:
                    j=j+1
                a=a+1
            
            if j<1:
                print(x)

o=prime([3,2,4,5,6,89,789])

o.filter()
o.filterlam()
                    
