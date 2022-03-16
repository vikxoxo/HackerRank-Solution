"""
Given an array of equal-length strings, you'd like to know 
if it's possible to rearrange the order of the elements in such a way 
that each consecutive pair of strings differ by exactly one character. 
Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
solution(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
solution(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character 
(eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.
"""
"""
Soln from 
https://benzene-dev.tistory.com/19
"""
from itertools import permutations

def check(s1, s2):
    count=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            count = count +1 
    if count!=1:
        return False
    
    return True
        
def solution(inputArray):
    pl= permutations(inputArray)
    
    for e in pl:
        ans=True
        for i in range(1,len(e)):
            if check(e[i],e[i-1])==False:
                ans= False
                break
        if ans == True:
            return ans
    
    return False
