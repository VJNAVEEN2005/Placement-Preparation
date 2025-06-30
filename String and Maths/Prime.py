n = int(input("Enter a number: "))

def prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n % i == 0: 
            return False
    return True

print(f"{n} is prime: {prime(n)}")  # Output: True or False based on the input