import random
a = []
for i in range(1,101):
    a.append(i)
#
result = random.sample(a,20)
print(result)

a = []
for i in range(1,11):
    a.append(i)
print(a)
result = random.sample(a,10)
print(result)