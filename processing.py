# CPU bounding tasks
import time
from multiprocessing import Process

results_task_1 = []
results_task_2 = []

def calculate_1(value):
    for i in range(1, value + 1):
        results_task_1.append(i ** 2)


def calculate_2(value):
    for i in range(1, value + 1):
        results_task_2.append(i ** 2)




# calculate_1(100000000)
# calculate_2(100000000)

# now = time.time()
# print("Elappsed time is: ", now - current)


if __name__ == "__main__":
    current = time.time()
    task_1 = Process(target=calculate_1, args=(500000,))
    task_2 = Process(target=calculate_2, args=(500000,))
    task_3 = Process(target=calculate_1, args=(500000,))
    task_4 = Process(target=calculate_2, args=(500000,))

    task_1.start()
    task_2.start()
    task_3.start()
    task_4.start()

    task_1.join()
    task_2.join()
    task_3.join()
    task_4.join()

    now = time.time()
    print("Elappsed time is: ", now - current)

