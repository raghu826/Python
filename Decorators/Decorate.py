import time


def update(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner

@update
def smthng(num):
    print("Hello world", num)

# ****************************************************


def time_it(func):
    def wrapper():
        start = time.time()
        print(start)
        func()
        end = time.time()
        print(end)
        print(f"total time is {(end-start)*1000}  milli secs")
    return wrapper


@time_it
def something():
    for i in range(1000000):
        if i == 999999:
            print(i)


if __name__ == '__main__':
    smthng(2)
    something()
