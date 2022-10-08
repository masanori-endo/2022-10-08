def prime_numbers_v1(numbers):
    prime = []
    for x in range(2, numbers):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime.append(x)
    return prime



def prime_number_v2(number):
    prime = []
    cashe = {}
    for x in range(2, number):
        if cashe.get(x) is False:
            continue
        else:
            prime.append(x)
            for y in range(x*2, number, x):
                cashe[y] = False
    return prime

print(prime_numbers_v1(100))
print(prime_number_v2(100))


