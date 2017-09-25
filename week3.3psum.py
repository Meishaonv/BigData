#Python
import time
def comput_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + 1.0/(i*i)
    return sum
start_time = time.time()
for counter in range(500):
    comput_sum(10000)
finish_time = time.time()
print comput_sum(10000)
print"Python running time: %s sec"%(finish_time - start_time)


