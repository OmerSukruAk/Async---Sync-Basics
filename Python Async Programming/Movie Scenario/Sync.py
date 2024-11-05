import asyncio
import time

start = time.time()
async def get_movie_tickets():
    print ("Getting movie tickets in 7 seconds"),
    await asyncio.sleep(7)
    print("Movie ticket had been bought")

async def like_instagram_posts():
    print("Stared liking instagram posts in 3 seconds")
    await asyncio.sleep(3)
    print("Post liking completed")

async def main():
    await get_movie_tickets()
    await  like_instagram_posts()
    print("All operations are completed")


asyncio.run(main()) 

end = time.time()

print(end-start)

