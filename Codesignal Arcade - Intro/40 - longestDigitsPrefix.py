"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
3 ≤ inputString.length ≤ 100.

[output] string
"""

def solution(inputString):
    inputString = list(inputString)
    ils = []
    # for i in range(len(inputString)):
    i=0
    if inputString[i].isdigit():
        il = [inputString[i]]
        for j in range(i+1,len(inputString[i:])):
            if inputString[j].isdigit()==True:
                il.append(inputString[j])
            elif inputString[j].isdigit()==False:
                break
        # ils.append(''.join(il))
        return ''.join(il)
    else:
        return '' 
        
 def longestDigitsPrefix(inputString):
    count = 0
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            count += 1
        else:
            return inputString[0:count]
    return inputString


