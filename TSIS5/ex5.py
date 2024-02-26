import re

s = "aavvvvbb abboba 1234a..s569a  ab a_z abbb ab .  b..........bb is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"


#ex5
p = re.compile('^a.*b$')
m = p.match(s)
print(m)