import re

hand = open('/home/talhajavaidmalik/Python for Everybody/Using Python to Access Web Data/Week1/myfile.txt')

numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('NumList:::::::::::::::::::' , numlist)
print('Maximum:', max(numlist))
