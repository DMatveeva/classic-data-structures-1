import time


a = []
i = 0
start_time = time.time()
while i < 20_000:
    a.append(i)
    i += 1
print("--- %s seconds ---" % (time.time() - start_time))
print(len(a))
