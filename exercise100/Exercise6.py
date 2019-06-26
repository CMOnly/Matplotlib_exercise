import time
import datetime
def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)
##print(Fib(int(input())))

#multiple
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = %d ' %(i, j, i*j),end = ' ')
    print()

import time

for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)

