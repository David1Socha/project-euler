def generate_even_fibonacci_numbers(n):
    list_even_fibonaccis = []
    if (n > 1):
        list_even_fibonaccis.append(2)
        two_previous_fibonacci = 1
        previous_fibonacci = 2
        fibonacci = 3
        while fibonacci < n: #this is wrong, should be while fibo less than n
            fibonacci = two_previous_fibonacci + previous_fibonacci
            two_previous_fibonacci = previous_fibonacci
            previous_fibonacci = fibonacci
            if (fibonacci%2 == 0):
                list_even_fibonaccis.append(fibonacci)
    return list_even_fibonaccis

def solve_problem():
    list_even_fibonaccis = generate_even_fibonacci_numbers(4000000)
    print(sum(list_even_fibonaccis))

solve_problem()
