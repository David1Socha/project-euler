def is_palindrome(n):
    is_palindrome = False
    string_num = str(n)
    if (string_num == string_num[::-1]):
        is_palindrome = True
    return is_palindrome

def largest_palindrome(digits): #returns largest palindrome made from product of 2 n-digit numbers
    largest_palindromes = []
    for i in reversed(range((10**digits))):
        for j in reversed(range((10**digits))):
            if is_palindrome((i*j)):
                largest_palindromes += [i*j]
                break
    return max(largest_palindromes)

def solve_problem():
    print(largest_palindrome(3))

solve_problem()
