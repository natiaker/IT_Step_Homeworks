# დაწერეთ ასინქრონული ფუნქცია, დააბრუნებს ატრიბუტად გადაწოდებული რიცხვის კვადრატს,
# იმ შემთხვევაში თუ ეს რიცხვი არის ლუწი, ამის შესამოწმებლად დაწერეთ მეორე ასინქრონული ფუნქცია.
# შესამოწმებლად შექმენით რამდენიმე თასქი, გამოიყენეთ gather მეთოდი

import asyncio


# define an asynchronous function to calculate the square of a number if the number is even
async def square(n):
    # await is_even coroutine to check if the number is even
    if await is_even(n):
        print(f"{n} * {n} = {n ** 2}")
    else:
        print(f"{n} is not even")


# async function to check if number is even
async def is_even(n):
    return n % 2 == 0


async def main():
    tasks = []

    for i in range(1, 10):
        task_number = i
        tasks.append(square(task_number))  # add tasks to calculate squares

    # run the tasks concurrently and await their completion
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
