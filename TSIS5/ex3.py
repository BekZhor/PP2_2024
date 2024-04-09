import re

s = "aavvvvbb abboba 1234a..s569a  ab a-z abbb ab .  ADSD-Ads  234fds-543ff --- gff---gfc rr-5 is presidents n,ame om AMiErIco aha ,,,,, hahahha ++#"



result = re.findall(r"[a-z]+[-][a-z]+", s) 
print(result)