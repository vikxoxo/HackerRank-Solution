"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""
def solution(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i]==elemToReplace:
            inputArray[i]=substitutionElem
    return inputArray

def solution2(i, e, s):
    return [x if x!=e else s for x in i]
