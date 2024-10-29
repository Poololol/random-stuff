import concurrent.futures
import time
numThreads = 10
r = [[j for j in range(numThreads)] for i in range(numThreads)]
def fun(i):
    a=i[0]
    b=i[1]
    print('s', a)
    time.sleep(1)
    r[a][b] = a*b
    print('f', a)
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=numThreads**2) as executor:
        for x in range(numThreads):
            for y in range(numThreads):
                executor.submit(fun, (x,y))
    print(r)