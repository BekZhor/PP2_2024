import os

if os.path.exists(r"c:\Users\Lenovo\Documents\jkl\op.txt"):
    print("yes")
f=open(r"c:\Users\Lenovo\Documents\jkl\op.txt","r")
if f:
    print("yes")
f.close()
f=open(r"c:\Users\Lenovo\Documents\jkl\op.txt","w")
if f:
    print("yes")
f.close()