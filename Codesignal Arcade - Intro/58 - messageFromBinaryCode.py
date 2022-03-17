"""
each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.

Example

For code = "010010000110010101101100011011000110111100100001", the output should be
solution(code) = "Hello!".

The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 
72 stands for H in the ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.
"""
def solution(code):
    phrase = ""
    # print(int('010',2)) -> easy binary to decimal in python
    bits = [int(code[i*8:i*8+8],2) for i in range(len(code)//8)]
    for j in range(len(bits)):
        phrase += chr(bits[j])
    return phrase
