# # # https://py.checkio.org/mission/pawn-brotherhood/
# #
# # Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules. It has various units with a wide range of movement patterns allowing for a huge number of possible different game positions (for example Number of possible chess games at the end of the n-th plies.) For this mission, we will examine the movements and behavior of chess pawns.
# #
# # Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row than their.
# #
# # A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.
#
# 这里写图片描述
# 题目意思是给定一个8*8的棋盘，
# 同时给定8个棋子的位置。
#  如果某一个棋子的位置可以由其他棋子一步到达，
# 则认为该棋子安全。判断8个棋子中安全的棋子的个数。
# 如图所示，左边的安全棋子个数为6，右边的位1。
# sq='abcdefgh'
# data={"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
# data=sorted(data,key=lambda x:x[1])
#
# chars=[]
# def safe_position(x):
#
#
# safe_position('a5')
# for i in data:
#     safe_position(i)
# print(chars)
# safe_pawns=list(filter(lambda x:x in chars,data))
# print(safe_pawns)
#
#
# # print(list(data_dict.keys()),list(data_dict.values()))

def safe_pawns(pawns):

    sq = 'abcdefgh'
    pawns = sorted(pawns, key=lambda x: x[1])

    chars = []
    for x in pawns:
        if x[0] == 'a':
            chars.append(sq[sq.index(x[0]) + 1] + str(int(x[1]) + 1))
        elif x[0] == 'h':
            chars.append(sq[sq.index(x[0]) - 1] + str(int(x[1]) + 1))
        else:
            chars.append(sq[sq.index(x[0]) + 1] + str(int(x[1]) + 1))
            chars.append(sq[sq.index(x[0]) - 1] + str(int(x[1]) + 1))

    safepawns = list(filter(lambda x: x in chars, pawns))

    return len(safepawns)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
