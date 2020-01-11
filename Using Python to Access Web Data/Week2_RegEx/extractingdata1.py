import re
# matching and extracting numbers
#[0-9] one digit
# + means that it will give the one or more digit

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)