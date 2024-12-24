def is_prime_all(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# Example usage
n = 29
print(f"Is {n} prime? {is_prime_all(n)}")
