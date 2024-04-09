mystr="sdkcmvGHLMNHJKLMN"
y=0
z=0
for x in mystr:
    if x.islower() :
        y+=1
    else:
        z+=1

print(y,z)