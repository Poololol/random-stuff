import asyncio
import time
import pygame
t1 = time.time()
def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped
@background
def main(x):
    pygame.time.delay(1000)
    print(x)

loop = asyncio.get_event_loop()
looper = asyncio.gather(*[main(x) for x in range(5)])
loop.run_until_complete(looper)
t2 = time.time()
print(t2-t1)