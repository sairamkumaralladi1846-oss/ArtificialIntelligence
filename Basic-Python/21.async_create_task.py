import asyncio

async def func1():
    await asyncio.sleep(1)
    print("func1")

async def func2():
    await asyncio.sleep(3)
    print("func2")

async def func3():
    await asyncio.sleep(2)
    print("func3")

async def main():
    # tasks = [asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())]
    # # Wait for all tasks to complete
    # await asyncio.gather(*tasks)
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    task3 = asyncio.create_task(func3())
if __name__ == "__main__":
    asyncio.run(main())
