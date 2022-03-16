"""
The pixels in the input image are represented as integers. 
The algorithm distorts the input image in the following way: 
Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself.
All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be solution(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. 
The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
the output should be

solution(image) = [[5, 4], 
                  [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output. 
To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. 
The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.
"""

def solution(image):
    ans = []
    for i in range(len(image) - 3 + 1):
        row = []
        for j in range(len(image[0]) - 3 + 1):
            s = image[i][j] + image[i+1][j] + image[i+2][j] + image[i][j+1] + image[i+1][j+1] + image[i+2][j+1] + image[i][j+2] + image[i+1][j+2] + image[i+2][j+2]
            
            row.append(int(s/9))
        ans.append(row)
    
    return ans
