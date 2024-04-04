# დაწერეთ ორი ასინქრონული ფუნქცია, ერთ-ერთი დააყოვნეთ 2 წამი, მეორე 5 წამი,
# დაბეჭდეთ მათი დაწყება და დასრულება, თასქები შექმენით ცალ-ცალკე და გაუშვით.


import asyncio
import time


# create 2 async functions: func1 and func2
async def func1():
    print("Start func1")
    await asyncio.sleep(2)
    print("Finish func1")


async def func2():
    print("Start func2")
    await asyncio.sleep(5)
    print("Finish func2")


async def main():
    start_time = time.time()

    # create task1 and task2 coroutine
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())

    # await task1 and task2 to finish
    await task1
    await task2

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time: .2f} Seconds")


if __name__ == "__main__":
    asyncio.run(main())