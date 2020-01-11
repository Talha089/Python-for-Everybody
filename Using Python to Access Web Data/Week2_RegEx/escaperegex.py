# If you want a specical regular expression character to just behave normally(most of the time)you prefix with '\'

import re

x = 'We just recieved $10.00 for cookies.'
y = re.findall('\$[0-9]+', x)
print(y)

#14:38