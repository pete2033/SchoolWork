from Test3 import addstuff 

addstuff(1,2)

from Test3 import breakstuff

breakstuff(3,2)

import re 
str="Hello #Raza!@#$%"
print(re.findall(r'\W', str))
print("How many non alha numerics exist?:\n",len(re.findall(r'\W', str)))
