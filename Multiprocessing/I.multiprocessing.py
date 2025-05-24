# In this code we will download multiple file using multiprocessing

import requests
import multiprocessing


def downloadFile(url, name):
    print(f"Download started for {name}")
    response = requests.get(url)
    open(f"files/{name}.jpg", "wb").write(response.content)
    print(f"Download Completed {name}")


if __name__ == "__main__":
    url = "https://picsum.photos/200/300"  #This link will generate random image everytime it hits.
    pros = []
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()


# Output:
# Download started for 0
# Download started for 1
# Download started for 3
# Download started for 4
# Download started for 2
# Download Completed 1
# Download Completed 2
# Download Completed 0
# Download Completed 3
# Download Completed 4




