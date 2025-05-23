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

# Output:
    # Sleeping for 4 seconds.
    # Sleeping for 2 seconds.
    # Sleeping for 1 seconds.
    # Time taken to run all 3 functions: 7.006099754999923
