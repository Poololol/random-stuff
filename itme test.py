from datetime import datetime
import time
def checkSleep(loops, sleepTime):
    error = 0
    for x in range(loops):
        t0 = time.time()
        time.sleep(sleepTime)
        t1 = time.time()
        error += (t1-t0)
    error/=loops
    print(f"Average error is {error}ms")
checkSleep(15, .5)