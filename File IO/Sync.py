import time

start = time.time()
def download_file(filename):
    print("file download started")
    time.sleep(3) # demonstrate the file time to download
    print("file Dowloaded :)")

# Download 3 identical files

def main():
    for x in range (3):
        download_file("")


if __name__ == "__main__":
    main()
    end = time.time()
    print("Time taken" , (end-start))