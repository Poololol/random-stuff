full = []
zero = []
real = []
for e in range(10):
    for v in range(10):
        for i in range(10):
            for f in range(10):
                if (e*e)%10 != f:
                    continue
                if (f*e)%10 != e:
                    continue
                if (v*e)%10 != i:
                    continue
                if (i*e)%10 != v:
                    continue
                full.append(1000*f+100*i+10*v+e)
                if f==i:
                    continue
                if f==v:
                    continue
                if f==e:
                    continue
                if i==v:
                    continue
                if i==e:
                    continue
                if v==e:
                    continue
                zero.append(1000*f+100*i+10*v+e)
                if f<4:
                    continue
                real.append(1000*f+100*i+10*v+e)
print(full, len(full))
print(zero, len(zero))
print(real, len(real))