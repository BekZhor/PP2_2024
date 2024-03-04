h = 0
c = input(str())
for i in c :
    if i >= "A" and i <= "Z" :
        h = h + 1
    if i >= "a" and i <= "z" :
        h = h + 1

print(h)