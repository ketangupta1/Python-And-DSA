import requests
from concurrent.futures import ProcessPoolExecutor


def downloadFile(url, name):
    print(f"Download started for {name}")
    response = requests.get(url)
    open(f"files/{name}.jpg", "wb").write(response.content)
    print(f"Download Completed {name}")



url = "https://picsum.photos/20/30"  #This link will generate random image everytime it hits.
pros = []
with ProcessPoolExecutor() as executor:
    l1 = [url for _ in range(6)]
    l2 = [i for i in range(6)]
    results = executor.map(downloadFile, l1, l2)  # We have to provide arguments in list so l1 and l2 are the arguments.
