import time


from functools import lru_cache

@lru_cache(maxsize=None) 
def fibo(x):
    if x<=1:
        return x
    else:
        return(fibo(x-1)+fibo(x-2))
    
n=int(input(">> : "))

n1 = time.time()
for i in range(n):
    print("\n", i, "\n")
    print(fibo(i), end=' ')

n2 = time.time()
print("\n",n2-n1)
print(fibo.cache_info())


import random


import time
time.sleep(0.1)


from tqdm import tqdm
for _ in tqdm(range(10), mininterval=0.00001, ncols=100, desc="Starting Quiz...  "):
        time.sleep(0.03)


import os
os.system('cls' if os.name == 'nt' else 'clear')