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
    
    asyncio.gather(get_movie_tickets(),like_instagram_posts())

    print("All operations are completed")


asyncio.run(main()) 

end = time.time()

print(end-start)

""""
cinema line takes 7 seconds
instagram post takes 3 seconds

sync
7+3 = 10 seconds

after async
line entrance t
open phone 
go to instagram
like post for 3 seconds (t+3)
wait in the line for 4 seconds (t+7)
in t+7 I have completed all my tasks
"""

"""
File download operation takes 3 seconds in 1 thread

if I have 10 seconds 
sync:
30 seconds approx

async:
3 seconds approx
"""

