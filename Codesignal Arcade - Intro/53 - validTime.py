"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
"""
def solution(time):
    l = time.split(':')
    
    if 0<=int(l[0])<=23 and 0<=int(l[1])<=59:
        return True
    else:
        return False
