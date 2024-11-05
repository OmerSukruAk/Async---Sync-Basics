import asyncio
import time

async def square(num):
    return num * num

async def main():
    x = await square(3)
    print (x)

    y = await square(4)
    print (y)

    z = x + y
    print (z)

asyncio.run(main())
