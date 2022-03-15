"""Given an array of strings, return another array containing all of its longest strings.
Example:
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"]."""

def solution(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r
   
def solution2(inputArray):
    maxe = max(inputArray, key = len)
    sol = []
    for i in range(len(inputArray)):
    
        if len(inputArray[i]) == len(maxe):
            sol.append(inputArray[i])
    return sol
        
