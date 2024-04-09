def gen(n):
    for i in range(n):
        a=i**2
        yield a

n=int(input())

for x in gen(n):
    print (x)