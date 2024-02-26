import re

s = "aavvvvbb abboba 1234a..s569a  ab a_z abbb ab .  b..........bb is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"


#ex6
x = re.sub(r'[ .,]', ':', s)
print(x)