def fibonacci_list_comprehension_terms(n):
    a, b = 0, 1
    return [a := b, b := a + b][0] for _ in range(n)]

def fibonacci_list_comprehension_max_value(max_value):
    a, b = 0, 1
    fib_sequence = []
    while a < max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
n_terms = 10
max_value = 100
print(f"Fibonacci sequence up to {n_terms} terms: {fibonacci_list_comprehension_terms(n_terms)}")
print(f"Fibonacci sequence less than {max_value}: {fibonacci_list_comprehension_max_value(max_value)}")
