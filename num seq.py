l = []
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if b+c!=a: continue
            if c>b: continue
            for d in range(1, 10):
                if c+d!=b: continue
                if d>c: continue
                if d==c: continue
                l.append(1000*a+100*b+10*c+d)
print(l)