#Not all regular expression repeats code are greedy! 
#IF you add a ? in character, the + and *
#chill out a bit...

import re

x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y) 