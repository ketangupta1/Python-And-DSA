from concurrent.futures import ThreadPoolExecutor
import time

class Test:
    def func(self, seconds):
        print(f"Sleeping for {seconds} seconds.")
        time.sleep(seconds)
        return seconds

test = Test()
with ThreadPoolExecutor() as executor:
    seconds_list = [1, 5, 3, 2]

    # It will call all the function parallelly and will return the value whenever execution completes.
    results = executor.map(test.func, seconds_list)
    for result in results:
        print(result)

# Output:
#   Sleeping for 1 seconds.
#   Sleeping for 5 seconds.
#   Sleeping for 3 seconds.
#   Sleeping for 2 seconds.
#   1
#   5
#   3
#   2
