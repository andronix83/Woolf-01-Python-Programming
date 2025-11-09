from typing import Callable

type FibonacciFunc = Callable[[int], int]
type IntCache = dict[int, int]

def caching_fibonacci() -> FibonacciFunc:
    """
    Returns the fibonacci numbers calculation function
    that supports results caching.
    :return: fibonacci function
    """
    # Cache for previously calculated results
    cache: IntCache = {}

    # Nested function that has access to the cache
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0 # first base case
        elif n == 1:
            return 1 # second base case
        elif n in cache:
            return cache[n] # return from cache
        else:
            # Calculate the value and save it in the cache
            result: int = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result
            return result

    return fibonacci


def main() -> None:
    # Getting the fibonacci function
    fib: FibonacciFunc = caching_fibonacci()

    print(fib(10)) # Should return 55
    print(fib(15)) # Should return 610
    print(fib(20)) # Should return 6765


if __name__ == "__main__":
    main()
