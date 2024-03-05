#ex5
a = int(input())
def from_n_to_zero(a) : 
    j = a
    while j != -1 :
        yield j
        j = j - 1

h = from_n_to_zero(a)

for i in from_n_to_zero(a) :
    print(i, end=" ")