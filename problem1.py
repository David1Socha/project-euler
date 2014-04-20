def is_multiple(x,n):
    return x%n == 0

def solveProblem():
    sum = 0
    for i in range(0,1000):
        if (is_multiple(i,3) or is_multiple(i,5)):
            sum += i
    return sum

print(solveProblem())
