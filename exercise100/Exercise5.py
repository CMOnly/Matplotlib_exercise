import random

def getrandomlist(*x):
    randomlist = []
    if len(x[0]) == 1:
        randomlist.append(random.randint(1))
    elif len(x[0]) == 2:
        for i in range(x[1]):
            randomlist.append(random.randint(x[0][0]))
    elif len(x) == 3:
        for i in range(x[1]):
            randomlist.append(random.randint(x[0][0],x[0][1]))
    else:
        print('please input your parameter correctly:[start = 0, end , number')
        return []

def sortlist(x):
    if len(x)<2:
        return x
    else:
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[i] > x[j]:
                    tem = x[i]
                    x[i] = x[j]
                    x[j] = tem
                elif x[i] == x[j]:
                    x.pop(j)
                else:
                    pass
    return x
def transFrmstr2dig(str):
    tem = str.split(",")
    return [int(tem[x]) for x in range(len(tem))]
print('please inout those parameter:')

rdlst = getrandomlist(transFrmstr2dig(input()))


print(sortlist(rdlst))