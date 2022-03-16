"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
10 ≤ n ≤ 106.

[output] integer
"""
def solution(n):
    n = str(n)
    l = [int(n[1:])]+[int(n[0:len(n)-1])]+[int(n[:k]+n[k+1:]) for k in range(1,len(n)-1)]
    print(l)
    return max(l)
    
 def solution2(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))
