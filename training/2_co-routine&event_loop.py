import asyncio

# Define your coroutine
async def my_coroutine():
    print("Hello, asyncio!")
    import time
    time.sleep(1)

async def my_coroutine2(a,b):
    print(a+b)

# Get the current event loop
loop = asyncio.get_event_loop()

# If the loop is not already running, you can schedule your coroutine with it
if not loop.is_running():
    loop.run_until_complete(my_coroutine())
    loop.run_until_complete(my_coroutine2(3,5))
