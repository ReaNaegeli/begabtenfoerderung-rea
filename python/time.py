ts = time.time()
print (ts)

print(round(ts, 2))

startTime = time.time()
time.sleep(2.4)
stopTime = time.time()

usedTime = stopTime - startTime

print(round(usedTime, 3))