str = input()

zeroGroup = 0
oneGroup = 0

last = str[0]
for i in range(len(str)):
    if last != str[i]:
        if last == '0':
            zeroGroup += 1
        elif last == '1':
            oneGroup += 1
    last = str[i]

if str[-1] == '0':
    zeroGroup += 1
else:
    oneGroup += 1

print(min(zeroGroup, oneGroup)) 
