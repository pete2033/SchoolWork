from Test3 import addstuff 

addstuff(1,2)

from Test3 import breakstuff

breakstuff(3,2)

import re 
str="Hello #Raza!@#$%"
print(re.findall(r'\W', str))
print("How many non alha numerics exist?:\n",len(re.findall(r'\W', str)))


import calendar
from datetime import date
from datetime import time
calendar.isleap(1900)
yy=2026
mm=11
print(calendar.month(yy,mm))
print(calendar.isleap(2028))
print(calendar.calendar(2026))
today=calendar.weekday(2026,11,6)
daysOFWeek={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday","5":"Saturday",6:"Sunday"}
print(daysOFWeek[today])
now=date.today()
print(now)
now.weekday()
print(calendar.day_name[now.weekday()])

noon=time(12,0,0)
noon.hour
noon.minute
noon.second

