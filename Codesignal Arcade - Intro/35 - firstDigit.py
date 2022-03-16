"""
Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
solution(inputString) = '1';
For inputString = "q2q-q", the output should be
solution(inputString) = '2';
For inputString = "0ss", the output should be
solution(inputString) = '0'.

"q22_34"
soln = '2' 
not '22'
"""

def solution(inputString):
    inputString = list(inputString)
    print(inputString)
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            return inputString[i]
            # print('i ', i)
            # for j in range(i+1, len(inputString[i+1:])):
            #     print('j', j)
            #     if inputString[j].isdigit()==False:
            #         print(inputString[j])
            #         return ''.join(inputString[i:j])
            break
