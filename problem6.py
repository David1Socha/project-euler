def sum_of_squares(n): #returns sum of squares of first n natural numbers
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i**2)
    print(sum)
    return sum

def square_of_sum(n): #returns square of sum of first n natural numbers
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum**2

def solve_problem():
    print(square_of_sum(100) - sum_of_squares(100))

solve_problem()
