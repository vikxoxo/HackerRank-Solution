"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc".

See https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
"""

from itertools import groupby
def lineEncoding(s):
    s2 = ""
    for k,g in groupby(s):
        l = len(list(g))
        if l == 1:
            s2 += k
        else:
            s2 += str(l) + k
    return s2
