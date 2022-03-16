"""
In the popular Minesweeper game you have a board with some mines and 
those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells.
Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
"""
def solution(matrix):
    row = len(matrix)
    col = len(matrix[0])
    def neighbouring_squares(i,j):
    #how?????
        return (sum(matrix[x][y]    for x in range(i-1,i+2) if 0 <= x < row
                                    for y in range(j-1,j+2) if 0 <= y < col
                                    if i != x or j != y))
    return [[neighbouring_squares(i,j) for j in range(col)] for i in range(row)]
