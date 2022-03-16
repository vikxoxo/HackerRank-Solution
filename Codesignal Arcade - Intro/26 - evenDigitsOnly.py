"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
"""
def solution2(n):
    return all([int(i)%2==0 for i in str(n)])
    
def solution(n):
    l = list(str(n))
    flag = True
    
    for i in l:
        if int(i)%2!=0:
            flag = False
    return flag
