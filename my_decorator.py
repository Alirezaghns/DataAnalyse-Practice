import time


def first_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start counting...")
        started_at = time.time()
        func(*args, **kwargs)
        finished_at = time.time()
        print(f"The {func.__name__} took {finished_at - started_at} seconds to run")
    return wrapper


@first_decorator
def sum_numbers():
    sum = 0
    for i in range(100000000):
        sum += i
    print(f"Retuls is: {sum}")


sum_numbers()


