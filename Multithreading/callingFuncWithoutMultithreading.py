import time

class Test:
    def func(self, seconds):
        print(f"Sleeping for {seconds} seconds.")
        time.sleep(seconds)

test = Test()

time1 = time.perf_counter()

test.func(4)
test.func(2)
test.func(1)

time2 = time.perf_counter()

print(f"Time taken to run all 3 functions: {time2-time1}")
