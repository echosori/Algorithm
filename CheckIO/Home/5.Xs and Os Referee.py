# # # Tic-Tac-Toe, sometimes also known as Xs and Os,
# is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid.
# The player who succeeds in placing three respective marks in a horizontal, vertical,
# or diagonal rows (NW-SE and NE-SW) wins the game.
# # #
# # # But we will not be playing this game.
# You will be the referee for this games results.
# You are given a result of a game and you must determine
# if the game ends in a win or a draw as well as who will be the winner.
# Make sure to return "X" if the X-player wins and "O" if the O-player wins.
# If the game is a draw, return "D".
# # A game's result is presented as a list of strings,
# where "X" and "O" are players' marks and "." is the empty cell.
# #
# # Input: A game result as a list of strings (unicode).
# #
# # Output: "X", "O" or "D" as a string.
# #
# # Example:
# #
# # checkio([
# #     "X.O",
# #     "XX.",
# #     "XOO"]) == "X"
# # checkio([
# #     "OO.",
# #     "XOX",
# #     "XOX"]) == "O"
# # checkio([
# #     "OOX",
# #     "XXO",
# #     "OXX"]) == "D"
# #
# # How it is used: The concepts in this task will help you when iterating data types.
# They can also be used in game algorithms, allowing you to know how to check results.
#
# Precondition:
# There is either one winner or a draw.
# len(game_result) == 3
# all(len(row) == 3 for row in game_result)


def checkio(game_result):
    for i in game_result:
        if len(set(i)) == 1 and set(i) != {'.'}:
            return i[0]
    a, b, c = game_result
    zipped = zip(a, b, c)
    for k in zipped:
        if len(set(k)) == 1 and set(k) != {'.'}:
            return k[0]
    if a[0] == b[1] == c[2] != '.' or a[2] == b[1] == c[0] != '.':
        return b[1]
    else:
        return 'D'

# CREATIVE
# def checkio(field):
#     for xo in 'XO':
#         if xo * 3 in field:
#             return xo
#         field = [''.join(elem) for elem in zip(*[list(line) for line in field])]
#         if xo * 3 in field:
#             return xo
#         if all(elem == xo for elem in [field[i][i] for i in range(3)]):
#             return xo
#         if all(elem == xo for elem in [field[i][2 - i] for i in range(3)]):
#             return xo
#     return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

