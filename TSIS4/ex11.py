#ex2
a = int(input())

def even(a) :
    for i in range(1,a+1) :
        if i % 2 == 0 :
            yield i

z = even(a)

for j in even(a) :
    print(next(z), end="")
    if j == a :
        break
    print(end=",")
