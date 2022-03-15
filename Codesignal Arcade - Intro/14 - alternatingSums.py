"""Several people are standing in a row and need to be divided into two teams. The first person goes into team 1,
the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.
You are given an array of positive integers - the weights of the people. Return an array of two integers,
where the first element is the total weight of team 1, and the second element is the total weight
of team 2 after the division is complete.
Example:
- For a = [50, 60, 60, 45, 70], the output should be alternatingSums(a) = [180, 105]."""

def solution2(a):

    return [sum(a[::2]),sum(a[1::2])]
  
def solution(a):
    t1 = 0
    t2 = 0
    for i in range(len(a)):
        if i%2==0:
            t1 = t1+a[i]
        else:
            t2 = t2+a[i]
    
    return [t1, t2]
