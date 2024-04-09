import os
os.chdir(r"c:\Users\Lenovo\Documents\jkl")
mystr="QWERTYUIOPASDFGHJKLZXCVBNM"
for  j in range(len(mystr)):
    h=mystr[j]
    g="{}.txt"
    k=g.format(h)
    f=open(k,"x")


f.close()


