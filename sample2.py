def prime_numbers_v1(numbers):
    prime = []
    for x in range(2, numbers):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime.append(x)
    return prime

print(prime_numbers_v1(1000))

