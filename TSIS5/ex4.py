
import re

s = "aavvvvbb abboba 1234a..s569a  ab a-z abbb  rr-5 is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"



result = re.findall(r"[A-Z][a-z]+", s) 
print(result)