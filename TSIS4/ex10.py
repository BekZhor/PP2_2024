#ex1
a = int(input())

def kvadrat(a) :
    for i in range(a) :
        yield pow(i,2)

z = kvadrat(a)

for j in kvadrat(a) :
    print(next(z))