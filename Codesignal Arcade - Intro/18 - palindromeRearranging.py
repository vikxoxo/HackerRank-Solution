"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""
   
def palindromeRearranging(inputString):
    odd_count = 0
    char_set = set(inputString)
    for i in char_set:
        char_count = inputString.count(i)
        if char_count % 2 != 0:
            odd_count += 1
    if odd_count <= 1:
        return True
    return False
