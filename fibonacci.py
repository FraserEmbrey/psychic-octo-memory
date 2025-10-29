"""
Fibonacci number generator module.
This module provides functionality to generate the nth Fibonacci number.

This implementation supports negative indices (negafibonacci) using the
identity::

    F(-n) = (-1)^{n+1} * F(n)

The function accepts integer inputs only (booleans are rejected).
"""


def fibonacci(n):
    """
    Generate the nth Fibonacci number.

    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    This function also supports negative indices using the negafibonacci
    identity: F(-n) = (-1)^{n+1} * F(n).

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)

    Returns:
        int: The nth Fibonacci number

    Raises:
        TypeError: If n is not an integer (booleans are rejected)
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")

    # Handle zero and one quickly
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Helper: compute F(k) for k >= 0 iteratively
    def _fib_nonnegative(k: int) -> int:
        a, b = 0, 1
        for _ in range(2, k + 1):
            a, b = b, a + b
        return b

    if n > 0:
        return _fib_nonnegative(n)

    # n < 0 -> use negafibonacci identity
    k = -n
    fk = _fib_nonnegative(k)
    # F(-k) = (-1)^{k+1} * F(k)
    sign = -1 if (k % 2 == 0) else 1
    return sign * fk


if __name__ == "__main__":
    # Example usage
    print("Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
