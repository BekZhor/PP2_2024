import re

s = "aavvvvbb abboba 1234a..s569a  ab a_z abbb ab .  b..........bb is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"


#ex4
result = re.findall(r'[A-Z][a-z]+', s)
print(result)
