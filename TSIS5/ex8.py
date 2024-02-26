import re

s = "aavvvvbb abboba 1234a..s569a  ab a_z abbb ab .  b..........bb is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"

#ex8
s = re.sub( r"([A-Z])", r" \1", s).split()
print(s)
