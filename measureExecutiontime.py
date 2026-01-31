import time

start_time= time.perf_counter()


# code here
for i in range(1000000):
    pass


end_time = time.perf_counter()


elapse_time = end_time  - start_time


print(f"Elapsed time  : {elapse_time :.1f} secods")