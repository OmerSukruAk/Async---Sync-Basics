import time
import asyncio

start = time.time()
async def download_file(filename):
    print("file download started")
    await asyncio.sleep(3) # demonstrate the file time to download
    print("file Dowloaded :)")

# Lets download 3 identical files
async def main():
    await asyncio.gather(download_file(""),download_file(""),download_file(""))

asyncio.run(main())

end = time.time()

print("Time taken" , (end-start))