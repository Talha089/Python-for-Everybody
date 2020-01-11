import re

#Starting at the beginning of the line, look for the string 'From'

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

y = re.findall('^From.*@([^ ]*)', line)
print(y)