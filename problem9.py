def is_pythagorean_triple(a,b,c): #Returns true iff a**2 plus b**2 equals c**2
    return (a**2) + (b**2) == (c**2)

def pythagorean_triple_summing(n): #Returns the pythagorean triple whose values sum to n
    a = 1
    found = False
    while (a < (n/3)):
        b=a
        while (b < (n/2)):
            c = n - b - a

            if is_pythagorean_triple(a,b,c):
                found = True
                break
            b+= 1
        if (found):
            break
        a += 1
    return [a,b,c]

def solve_problem():
    triple = pythagorean_triple_summing(1000)
    print(triple)
    print(triple[0] * triple[1] * triple[2])

solve_problem()
