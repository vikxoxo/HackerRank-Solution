"""
Given a string, find the shortest possible string which can be achieved by 
adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".
"""
def solution(st):
    for i in range(len(st)):
        sub = st[i:len(st)]
        if sub[::-1] == sub:
            missing = st[0:i]
            return st + missing[::-1]
    return st
