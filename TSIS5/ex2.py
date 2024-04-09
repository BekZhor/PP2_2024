import re

s = "aavvvvbb abboba 1234a..s569a  ab a_z abbb ab .  b..........bb is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"


#ex1
result = re.findall(r"[^ ]*ab{2,3}", s) 
print(result)