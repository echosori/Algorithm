def longest_palindromic(text):
    return text


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"

# Write a function that finds the longest palindromic substring of a given string.

# Try to be as efficient as possible!
#
# If you find more than one substring you should return the one which is closer to the beginning.
#
# Input: A text as a string.
#
# Output: The longest palindromic substring.
#
# Precondition: 1 < |text| ≤ 20
# The text contains only ASCII characters.
