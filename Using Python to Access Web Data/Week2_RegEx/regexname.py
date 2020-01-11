import re
# look through the string until you find @ sign
# [^ ] Everything but not including the space
# match many of them

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', line)
print(y)