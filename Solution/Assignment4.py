def reverse_string_join(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])

# Example usage
input_string = input("Enter a string: ")
print(f"Reversed string: {reverse_string_join(input_string)}")
