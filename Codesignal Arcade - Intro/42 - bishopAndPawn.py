"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:
"""
def solution(bishop, pawn):
    # print(ord('a')) -> 97

    if ord(bishop[0]) == ord(pawn[0]):
        return False
    else:
        bishop_elm = ord(bishop[0])+int(bishop[1])
        pawn_elm = ord(pawn[0])+int(pawn[1])
        return (bishop_elm + pawn_elm)%2 == 0
