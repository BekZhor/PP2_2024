class gen:

    def __init__(self,n):
        self.n=n


    def __iter__(self):
        self.n=n
        return self
    
    def __next__(self):
        x=self.n 
        self.n = self.n-1
        if x>=0:
            return x
        else:
            raise StopIteration
        

n=int(input())

t=gen(n)

it=iter(t)

for i in it:
    print(i)



