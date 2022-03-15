"""Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky
if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.
Example
- For n = 1230, the output should be isLucky(n) = true;
- For n = 239017, the output should be isLucky(n) = false."""

def solution(n):
    l = list(str(n))
    # print(l)
    if sum([int(i) for i in l[0:int(len(l)/2)]]) == sum([int(i) for i in l[int(len(l)/2):]]):
        return True
    else:
        return False

     
def solution2(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))
      
