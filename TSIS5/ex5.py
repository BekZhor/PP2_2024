import re

s = "lkjh fawedfvbb  ab v"



result = re.findall(r'[^ ]*a.*b',s) 
print(result)