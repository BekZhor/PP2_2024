def is_prime(num1) :
    if num1 < 2 :
        return False
    for i in range(2, int(num1 ** 0.5)+1):
        if num1 % i == 0:
            return False
    return True

def filter_prime(numbers) :
    return [num1 for num1 in numbers if is_prime(num1)]

numbers = [1,2,3,4,5,6,7,8,9]

filtered_primes = filter_prime(numbers)
print(filtered_primes)