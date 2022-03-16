"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), 
separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
solution(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
solution(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
solution(inputString) = false.
"""
def solution(inputString):
    if len(inputString)!=17:
        return False
    l = inputString.split('-')
    print('0 ' ,ord('0'))
    print('9 ' ,ord('9'))
    print('A ' ,ord('A'))
    print('F ' ,ord('F'))
    flag = True
    if len(l)!=6:
        return False
    for i in l:
        il = list(i)
        if len(il)<2:
            return False
        
        c01 = (ord('0')<=ord(il[0])<=ord('9'))
        
        c02 = (ord('A')<=ord(il[0])<=ord('F'))
        c11 = (ord('0')<=ord(il[1])<=ord('9'))
        c12 =  (ord('A')<=ord(il[1])<=ord('F'))
        
        print(c01)
        print(c02)
        print(c11)
        print(c12)
        print('-------------')
        if (c01 or c02)  & (c11 or c12)   != True:
            print('act')
            return False
            flag = False
            break
    return flag
