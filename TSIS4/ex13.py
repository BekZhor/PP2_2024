#ex4
a = int(input())
b = int(input())
def squares(a,b) :
    for i in range(a, b+1) :
        yield i ** 2 

z = squares(a,b)

for j in squares(a,b) :
    print(next(z),  end=" ")
