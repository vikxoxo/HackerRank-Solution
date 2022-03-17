"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. 
If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
solution(product) = 26;
For product = 19, the output should be
solution(product) = -1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer product

Guaranteed constraints:
0 ≤ product ≤ 600.

[output] integer
"""
def solution(p):
    if p == 0:
        return 10
    elif p == 1:
        return 1
    
    n = []

    while 1 < p:
        for d in range(9, 1, -1):
            if p % d == 0:
                p /= d
                n.append(d)
                break
        else:
            return -1

    return int(''.join(map(str, sorted(n))))
