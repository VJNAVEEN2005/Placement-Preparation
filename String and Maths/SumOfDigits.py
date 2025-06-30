def sumofDigits(n):
    if n < 0:
        n = -n
    sum = 0
    
    while n != 0:
        sum = sum + n % 10
        n = n // 10
    return sum

n = int(input("Enter a number: "))
print(f"Sum of digits of {n} is: {sumofDigits(n)}")

# Output: Sum of digits of n is: <calculated sum>
# Example: If n = 123, Output: Sum of digits of 123 is: 6
# Example: If n = -456, Output: Sum of digits of -456 is: 15
# Example: If n = 0, Output: Sum of digits of 0 is: 0