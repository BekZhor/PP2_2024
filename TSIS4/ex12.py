#ex3
a = int(input())
def divisibility_3_4(a) :
    for i in range(1, a+1) :
        if i % 3 == 0 and i % 4 == 0 :
            yield i

l = divisibility_3_4(a)

print(next(l))
print(next(l))
print(next(l))
print(next(l))
