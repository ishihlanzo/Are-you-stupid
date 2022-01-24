from time import time
IT = 100_000_000

start = time()
for i in range(IT):
    bool(i)
print(f"bool: {time()-start}s")

start = time()
for i in range(IT):
    not not i
print(f"not not: {time()-start}s")
