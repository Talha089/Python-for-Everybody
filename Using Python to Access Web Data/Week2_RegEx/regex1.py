import re

#using re.search Like  find()


#hand = open(filename)
# for line in hand :
        #line = rstrip()
        #if line.find('From:') >=0:
            #print(line)





hand = open('/home/talhajavaidmalik/Python for Everybody/Using Python to Access Web Data/Week1/myfile.txt')
for line in hand:
        line = line.rstrip()
        if re.search('From:', line):
            print(line) 