#The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string

import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y) 