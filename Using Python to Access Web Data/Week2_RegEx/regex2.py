#USING re.search() LIKE startswith()

#hand = open('/home/talhajavaidmalik/Python for Everybody/Using Python to Access Web Data/Week1/myfile.txt')
#for line in hand:
#    line = line.rstrip()
#    if line.startswith('From:'):
#        print(line)

import re

hand = open('/home/talhajavaidmalik/Python for Everybody/Using Python to Access Web Data/Week1/myfile.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:',line):
        print(line)
