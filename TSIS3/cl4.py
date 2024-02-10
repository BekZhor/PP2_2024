import math



class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self):
        print("(",self.x,";",self.y,")")
    
    def move(self,c,f):
        self.x=self.x+c
        self.y=self.y+f
        print("(",self.x,";",self.y,")")

    def dist(self,k,l):
        if self.x>k:
            j=((self.x-k)**2 + (self.y-l)**2)
            h=math.sqrt(j)
            print(h)
        else:
            j=((k-self.x)**2 + (l-self.y)**2)
            h=math.sqrt(j)
            print(h)

u=point(4,5)

u.dist(7,8)

u.show()

u.move(8,9)
