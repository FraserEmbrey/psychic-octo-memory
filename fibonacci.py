"""
Fibonacci number generator module.
This module provides functionality to generate the nth Fibonacci number.
"""


def fibonacci(n):
    """
    Generate the nth Fibonacci number.
    
    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Iterative approach for efficiency
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


if __name__ == "__main__":
    # Example usage
    print("Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
