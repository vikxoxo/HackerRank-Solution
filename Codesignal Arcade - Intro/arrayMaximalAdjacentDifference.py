"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
"""
def solution(inputArray):
    l = []
    for i in range(1, len(inputArray)):
        d = inputArray[i]-inputArray[i-1]
        if d>=0:
            l.append(d)
        else:
            d= d*(-1)
            l.append(d)
    return int(max(l))
