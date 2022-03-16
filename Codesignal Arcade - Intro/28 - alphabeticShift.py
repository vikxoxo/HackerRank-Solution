"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet;
i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
"""



def solution(inputString):
    return ''.join([chr(ord(c)+1) if c!='z' else 'a' for c in list(inputString)])
