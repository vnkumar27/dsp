# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

*Answer : 937 days*

*Code:*

from datetime import date

d0 = date(2013,01,02)
d1 = date(2015,07,28)
delta = d1 - d0
print (delta.days)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

*Answers: 513 days*

*Code:*

from datetime import date

d0 = date(2013,12,31)
d1 = date(2015,05,28)
delta = d1 - d0
print (delta.days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

*Answer: 7850 days*

*Code:*

from datetime import date

d0 = date(1994,01,15)
d1 = date(2015,07,14)
delta = d1 - d0
print (delta.days)

