mystr="abba"
y=1
z=0
for i in range(len(mystr)):
    if mystr[i]==mystr[len(mystr)-y]:
        y+=1
        z+=1
    if z==(len(mystr)/2):
        print("Palindrom")

