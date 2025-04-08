import asyncio

# define an asynchronous generator
async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield i
		
async def main():
    # create the iterator
    it = async_generator()
    result = await anext(it)

    print (result)

async def main_for():
    async for result in async_generator():
        print(result)

asyncio.run(main_for())