z = 1
def multi(x) :
    global z
    z = z * x
    return z

List = [4,5,6,7]
list(map(multi, List))
print(z)