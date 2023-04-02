import time


def timer(f, *args, **kwargs):
    start_time = time.time()
    f(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.6f} seconds")


timer(print, "Hello")
timer(zip, [1, 2, 3], [4, 5, 6])
timer("Hi {name}".format, name="Bug")