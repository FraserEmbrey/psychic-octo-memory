# psychic-octo-memory
This is a test repo for the Using AI for Efficient Coding workshop

## Fibonacci Number Generator

A Python project that generates the nth Fibonacci number when given a number n.

### Usage

```python
from fibonacci import fibonacci

# Get the 10th Fibonacci number
result = fibonacci(10)
print(result)  # Output: 55
```

Or run directly:
```bash
python3 fibonacci.py
```

### Running Tests

```bash
python3 -m unittest test_fibonacci.py -v
```

### Fibonacci Sequence

The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

Example sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
