import math
import datetime

answ = 0
while True:
    if (answ + 100 == pow(math.floor(math.sqrt(answ + 100)), 2)) and (answ + 168+100 == pow(math.floor(math.sqrt(answ +100+ 168)), 2)):
        print('the answer is :%d' % answ)
        break
    else:
        answ += 1


#exercise4

def isleapyear(x):
    if x % 400 == 0 or (x%4 == 0 and x%100 != 0):
        return True
    else:
        return False


time = input('please input time like 20190108:')
days = 0
factor = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
if(isleapyear(int(time[:4])) == True) and (int(time[4:6]) > 2):
    factor[1] = 29
else:
    pass
for i in range(int(time[4:6])):
    days += factor[i]

print('the time you enter is %dth in the year!' % (days + int(time[-2:])) )


