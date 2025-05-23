import threading
import time

class Test:
    def func(self, seconds):
        print(f"Sleeping for {seconds} seconds.")
        time.sleep(seconds)

test = Test()

time1 = time.perf_counter()

t1 = threading.Thread(target=test.func, args=[4])
t2 = threading.Thread(target=test.func, args=[2])
t3 = threading.Thread(target=test.func, args=[1])
t1.start()
t2.start()
t3.start()

time2 = time.perf_counter()

print(f"Time taken to run all 3 functions: {time2-time1}")

# Output: 
#   Sleeping for 4 seconds.
#   Sleeping for 2 seconds.
#   Sleeping for 1 seconds.
#   Time taken to run all 3 functions: 0.002374560999669484

# Here time taken is less than 1 sec it is because .start() will just call the function and move to the next line it will not wait till the execution of function.
# If you wants your thread to wait till execution of function then use .join() after starting the thread using .start()
# e.g: 
#   t1.start()
#   t1.join()
# Here thread t1 will wait till the execution of function
