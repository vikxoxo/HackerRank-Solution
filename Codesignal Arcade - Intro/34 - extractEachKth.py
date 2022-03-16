"""
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

Read this
https://www.geeksforgeeks.org/python-list-slicing/
"""
def solution(inputArray, k):
    l = []
    for i in range(len(inputArray)):
        if (i+1)%k!=0:
            l.append(inputArray[i])
        
    return l
def solution2(inputArray, k):
    del inputArray[k-1::k]
    return inputArray
