for i in range(100,1000):
    if i == (pow(i%10,3) + pow(i//100,3)+ pow((i%100)//10,3)):
        print(i)




j = 947
print(j%10, end = '')
print(pow(j%10,3))
print(j//100)
print((j%100)//10)
i = 153
if i == (pow(i % 10, 3) + pow(i // 100, 3) + pow((i % 100) // 10, 3)):
    print(i)

for i in range(100,1000):
    s=str(i)
    one=int(s[-1])
    ten=int(s[-2])
    hun=int(s[-3])
    if i == one**3+ten**3+hun**3:
        print(i)


import datetime
print(datetime.date.today())
print(datetime.date(2333,2,3))
print(datetime.date.today().strftime('%d/%m/%Y'))
day=datetime.date(1111,2,3)
day=day.replace(year=day.year+22)
print(day)

a=set(['x','y','z'])
b=set(['x','y','z'])
c=set(['x','y','z'])
c-=set(('x','z'))
a-=set('x')
for i in a:
    for j in b:
        for k in c:
            if len(set((i,j,k)))==3:
                print('a:%s,b:%s,c:%s'%(i,j,k))

#exercise

n = int(input('how many starts do you want to draw?'))

for i in range(n):
    print(' '*((n)*2-i), end = '')
    print('*'*(i*2-1))
for j in range(n):
    print(' '*(n+j-1), end=' ')
    print('*'*((n-j)*2-1))


def draw(num):
    b = num
    def subdraw(num):
        a = '*'*((b-num)*2+1)
        print(a.center(b*2,' '))
        if num != 1:
            subdraw(num-1)
            print(a.center(b*2,' '))
    subdraw(num)


draw(10)