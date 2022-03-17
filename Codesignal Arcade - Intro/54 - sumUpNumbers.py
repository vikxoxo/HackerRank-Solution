"""
Example

For inputString = "2 apples, 12 oranges", the output should be
solution(inputString) = 14.

pproach: The idea is to use Python re library to extract the sub-strings from the given string which match the pattern [0-9]+. 
This pattern will extract all the characters which match from 0 to 9 and 
the + sign indicates one or more occurrence of the continuous characters.

Below is the implementation of the above approach:
"""
import re
def solution(inputString):
    l = re.findall(r'[0-9]+', inputString)
    return sum([int(i) for i in l])
