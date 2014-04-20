def make_sieve_primes(n): #Returns a list of all primes below n
    primelist = list(range(0,n))
    prime = 2
    increment = 4
    while prime * prime <= (n-1):
        while True:
            try:
                primelist[increment] = 0
                increment += prime
            except IndexError:
                break
        while True:
            prime += 1
            if primelist[prime] != 0:
                break
        increment = prime * 2
    primelist = [x for x in primelist if x != 0]
    del primelist[0]
    return primelist



def solve_problem():
    sum_primes = sum(make_sieve_primes(2000000))
    print(sum_primes)

solve_problem()
