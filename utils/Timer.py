import timeit


def timer(func):
    def wrapper(*args, **kwargs):
        # start the timer
        start_time = timeit.default_timer()
        # call the decorated function
        result = func(*args, **kwargs)
        # remeasure the time
        end_time = timeit.default_timer()
        # compute the elapsed time and print it
        execution_time = end_time - start_time
        # return the result of the decorated function execution
        return execution_time * 10 ** 3
    # return reference to the wrapper function
    return wrapper
