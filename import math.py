import time
import math
l=[]
o=[]
t1 = time.time()
for x in range(2,101):
    for n in range(2, math.floor(math.log(10000, x))+1):
        m = x**n
        l.append(m)
        o.append((m, x, n))
print(time.time()-t1)
l.sort()
o.sort(key=lambda x: x[0])
print(len(set(l)))
#print(o[0:16])
j=[]
m=0
for _ in range(1):
    for x in range(2, 101):
        if x not in l:
            m+=int(math.log(10000, x)-1)
            j.append((x, int(math.log(10000, x))))
print(m, j)