import re

s = "aavvvvbb abboba 1234a..s569a  ab a_z abbb ab .  b..........bb is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"



x=re.findall("[A-Z][a-z]*",s)
z=""
print(x)
for i in x:
     z=z+i+" "
print(z)