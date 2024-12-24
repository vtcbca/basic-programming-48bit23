def alphabet_pattern_format(n):
    for i in range(1, n + 1):
        # Create the increasing part
        increasing = [chr(64 + j) for j in range(1, i + 1)]
        
        # Create the decreasing part
        decreasing = [chr(64 + j) for j in range(i - 1, 0, -1)]
        
        # Combine both parts
        line = " ".join(increasing + decreasing)
        
        # Print with formatting (right-aligned)
        print("{:>{width}}".format(line, width=2 * n - 1))

# Example usage
n = 3
alphabet_pattern_format(n)
