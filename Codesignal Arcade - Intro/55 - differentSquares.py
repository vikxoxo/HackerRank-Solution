"""

Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
"""

def solution2(matrix):
    s = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
                s.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(s)

def solution(matrix):
    us = []
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r-1):
        # rs = []
        for j in range(c-1):
            rs = []
            rs.append(matrix[i][j:j+2])
            rs.append(matrix[i+1][j:j+2])
            print('sqr ',rs)
        # if rs not in us :
            
            us.append(rs)
    # for i in range(len(us)):
    #     print(us[i])
    # s = set(us)
    uq=[]
    for i in us:
        if i not in uq:
            
            uq.append(i)
    # print(s)
    return len(uq)
