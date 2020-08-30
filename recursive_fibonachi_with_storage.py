"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions.
store intermediate values to avoid calculating them again.
this increases space complexity but reduces the time complexity.
"""

previous = {}


def get_fib(position):
    if position == 0 or position == 1:
        return position
    if position in previous:
        return previous[position]
    first = get_fib(position - 2)
    second = get_fib(position - 1)
    result = first + second
    previous[position] = result
    return result


# Test cases
print(get_fib(8))
print(get_fib(11))
print(get_fib(0))
