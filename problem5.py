def lcm(m,n): #returns least common multiple of m and n
    num = 0 
    is_lcm = False
    while (not is_lcm):
        num+= max(m,n)
        is_lcm = (not num%m) and (not num%n)
    return num
        

def smallest_divisible_by(n): #returns smallest positive number evenly divisble by numbers from 1 to n
    num = 1
    divisors = range(1,n+1)
    i = 0
    while (i < n):
        num = lcm(divisors[i],num)
        i+= 1
    return num

def solve_problem():
    print(smallest_divisible_by(20))

solve_problem()
