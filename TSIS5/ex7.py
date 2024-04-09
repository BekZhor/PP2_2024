import re

s = "my_variables_name"
f=""

for i in range(len(s)):
    if s[i] == '_':
        continue
    elif s[i] != '_' and s[i-1] == '_':
        g=s[i].upper()
        f=f+g
    elif s[i] != '_':
        f=f+s[i]


print(f)


