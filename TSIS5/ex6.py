import re

s = "lkjh fawedf,,vb..b  ab "



result = re.sub("[\s,.]",":",s) 
print(result)