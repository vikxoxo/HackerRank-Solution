"""Given two strings, find the number of common characters between them.
Example:
For s1 = "aabcc" and s2 = "adcaa", the output should be commonCharacterCount(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c"."""

def solution(s1, s2):
    cl = set(s1) & set(s2)
    s = 0
    for i in cl:
        s = s + min([s1.count(i),s2.count(i)])
    return s

def solution2(s1, s2):
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)
