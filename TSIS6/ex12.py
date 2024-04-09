f=open(r"c:\Users\Lenovo\Documents\jkl\op.txt","r")
g=open(r"c:\Users\Lenovo\Documents\jkl\O.txt","a")
for x in f:
    g.write(x)
g.close()
f.close()