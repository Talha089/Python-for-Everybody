#You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses

# /S atleast one non-whitespacec character
# y = re.findall('\S+@\S+',x)

import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)',x)
print(y)