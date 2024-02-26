import re

s = "aavvvvbb abboba 1234a..s569a  ab a_z abbb ab .  b..........bb is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"



#ex9
z = ""

s = re.sub( r"([A-Z])", r" \1", s).split()
for i in s :
     z = z + " " + i
print(z)