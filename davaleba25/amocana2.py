# დაწერეთ ფუნქცია, რომელსაც ატრიბუტად გადაეცემა  რიცხვებისგან შემდგარი Queue,
# ფუნქციამ უნდა დაბეჭდოს ნაკადის სახელი, რიგიდან ამოღებული მნიშვნელობა და არის თუ არა ეს რიცხვი ლუწი.
# გაუშვით სამი ნაკადი(thread) და მხოლოდ ამის შემდეგ შეავსეთ რიგი(queue). საბოლოოდ დააჯოინეთ და დაბეჭდეთ
# რომ ყველა ამოცანა შესრულებულია.
import random
import threading
from queue import Queue


def worker(num_queue):
    # Continuously process numbers from the queue until num is None
    while True:
        num = num_queue.get()  # get number from queue

        if num is None:
            break

        current_thread_name = threading.current_thread().name  # current thread name

        print(f'{current_thread_name}, Number: {num}, Number is even: {not num % 2}')
        # mark the task as done
        num_queue.task_done()


number_queue = Queue()  # create number queue
thread_number = 3
thread_list = []  # store thread objects
# create and start threads
for _ in range(thread_number):
    thread = threading.Thread(target=worker, args=(number_queue,))
    thread.start()
    thread_list.append(thread)

# generate random number list
numbers = [random.randint(1, 20) for i in range(10)]
print(f"numbers: {numbers}")

# add numbers from numbers list to the queue
for number in numbers:
    number_queue.put(number)

# add None value to queue to stop worker
for _ in range(thread_number):
    number_queue.put(None)

# wait all tasks to finish and then join to main thread
for thread in thread_list:
    thread.join()

print("Done!")



