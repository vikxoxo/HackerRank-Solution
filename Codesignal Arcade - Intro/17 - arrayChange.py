"""
You are given an array of integers. 
On each move you are allowed to increase exactly one of its element by one. 
Find the minimal number of moves required 
to obtain a strictly increasing sequence from the input.
"""
def solution(inputArray):
    f = inputArray[0]
    count = 0
    for i in inputArray[1:]:
        #if second element onward is small
        
        if i <= f:
            #make it big
            count = count + f - i + 1
            
            #make f big 
            # 2, 2, 3 
            # count inc by 1
            
            #6 2 4
            #2 -> 7 i.e. f+1
            f = f+1 
        else:
            f = i
    return count
