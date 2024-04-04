# დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს და დაბეჭდავს რიცხვებს 1-დან 10-მდე

import asyncio
import random
import time


# define an asynchronous function that will sleep for a random duration
async def func(n, delay):
    print(f"Started {n}")
    start_time = time.time()

    await asyncio.sleep(delay)

    end_time = time.time()
    print(f"Finished {n} in {end_time - start_time: .2f} Seconds")


# dfine main coroutine that will create and run the asynchronous tasks
async def main():
    tasks = []

    for i in range(1, 11):
        task_num = i
        delay = random.randint(1, 10)
        tasks.append(func(task_num, delay))

    # run the tasks concurrently and await their completion
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
