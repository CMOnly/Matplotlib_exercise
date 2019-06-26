sum = 0
a = 2
b = 1
for i in range(2):
    sum+= a/b
    tem = a+b
    b = a
    a = tem

print(sum)

