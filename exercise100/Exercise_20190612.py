origin_digital = ['1', '2', '3', '4']
n = len(origin_digital)
m = 0
results = []
for i in origin_digital:
    Hp = i
    t_origin_digital = origin_digital[:]
    t_origin_digital.pop(origin_digital.index(i))
    Tplst = t_origin_digital
    print(Tplst)
    for j in Tplst:
        Tp = j
        t_Tplst = Tplst[:]
        t_Tplst.pop(Tplst.index(j))
        Lp = t_Tplst
        for k in Lp:
            results.append(Hp+Tp+k)
print(results)


#answer
results = []
for i in range(1,5):
    for j in range(1, 5):
        for k in range(1,5):
            if ((i != k) and (j != k) and (i !=  j)):
                results.append(i*100 + j*10 +k)
print('the total combination is %d' % len(results))
print('the detail digital are as below:\n', results)


# exercise 2

profit = int(input('please input your company profit:'))
bonus = 0
if profit > 100:
    bonus = (profit-100)*0.01 + 40*0.015 + 20*0.03 + 20*0.05 + 10*0.075 + 10 * 0.10
elif profit >60:
    bonus = (profit - 60)*0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.10
elif profit > 40:
    bonus = (profit - 40)* 0.03 + 20 * 0.05 + 10 * 0.075 + 10 * 0.10
elif profit > 20:
    bonus = (profit - 20) * 0.05 + 10 * 0.075 + 10 * 0.10
elif profit > 10:
    bonus = (profit - 10)* 0.075 + 10 * 0.10
else:
    bonus = profit*0.1

print('your bonus is %f'% bonus)

#answer
profit = int(input('please tell me your profit:'))
threshold = [10,10,20, 20, 40]
rate = [0.1, 0.075, 0.05,0.03,0.015,0.01]
bonus = 0
for i in range(len(threshold)):
    if profit < threshold[i]:
        bonus += profit*rate[i]
    else:
        bonus += threshold[i]*rate[i]
        profit -= threshold[i]
bonus+=profit*rate[-1]
print('your bonus is %f'% bonus)


profit=int(input('Show me the money: '))
bonus=0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)
