import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# el mateix exemple, però ara les dues tasques s'executen concurrentment.

async def main():

    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # await task1
    await task2

    # await say_after(1, 'hello lloyd')
    # await say_after(2, 'world lloyd')

    print(f"finished at {time.strftime('%X')}")


# Alternativa moderna a l'ús de create_task()
"""
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")
"""


# Quan cridem say_after amb await, main() espera fins que la funció say_after s'ha executat.

"""
async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")
"""

asyncio.run(main())

