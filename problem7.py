def is_prime(n):
    is_prime = True
    if (n < 2):
        is_prime = False
    elif (n%2 == 0):
        is_prime = False
    elif (n > 2):
        i = 3
        while (i * i <= n and is_prime):
            if (n%i == 0):
                is_prime = False
            else:
                i+= 2
    return is_prime

def get_prime(n): #Returns nth prime number
    num_primes = 1
    i = 1
    while (num_primes < n):
        i += 2
        if is_prime(i):
            num_primes += 1
    return i

def solve_problem():
    print(get_prime(10001))

solve_problem()
