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

def get_prime_factors(n):
    prime_factors = []
    if (is_prime(n)):
        prime_factors += [n]
    else:
        i = 2
        continue_loop = True
        while i < n and continue_loop:
            if ((n%i)==0):
                prime_factors += [i]
                prime_factors += get_prime_factors(int(n/i))
                continue_loop = False
            i+=1
    return prime_factors

def solve_problem():
    print(get_prime_factors(600851475143))

solve_problem()
