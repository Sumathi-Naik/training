def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the upper limit to find prime numbers: "))


prime_numbers = []

for num in range(2, n + 1):
    if is_prime(num):
        prime_numbers.append(num)

print(f"Prime numbers between 0 and {n} are:",prime_numbers)