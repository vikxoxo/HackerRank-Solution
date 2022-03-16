"""

Codewriting

300

Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true
"""

def solution(cell1, cell2):
    # print(ord('A')) -> 65
    l1 = list(cell1)
    l2 = list(cell2)
    if ((ord(l1[0])+int(l1[1]))%2==0 and (ord(l2[0])+int(l2[1]))%2==0) or ((ord(l1[0])+int(l1[1]))%2!=0 and (ord(l2[0])+int(l2[1]))%2!=0):
        return True
    else:
        return False 

def solution2(cell1, cell2):
    
    return (ord(cell1[0])+int(cell1[1])+ord(cell2[0])+int(cell2[1]))%2==0
        
        
