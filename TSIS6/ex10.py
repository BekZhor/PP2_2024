f=open(r"c:\Users\Lenovo\Documents\jkl\op.txt","a")
mylist=[1,2,3,4,5,6]
mystr=str(mylist)

f.write(mystr)
f.close()
f=open(r"c:\Users\Lenovo\Documents\jkl\op.txt","r")
for x in f:
    print(x)
f.close()