"""
Let's deal with the simpler testing for palindrome first. Since a
palindrome reads the same from either direction, the first letter must
be the same as the last letter, and so on. We could run the this test
from the first to the last letter, but we really only need to run it on
1/2 of the input string.

To simply the test, I propose to remove all spaces from a string, and
have that as our input for question 2, and hence our palindrome tester.
"""

def is_palindrome(s):
    half = len(s) // 2

    for i in range(half - 1):
        if s[i] != s[-i]:
            return False

    return True

# Odd lengthed string
assert(is_palindrome("bob"))

# Even lengthed string
assert(is_palindrome("gg"))

# Empty string
assert(is_palindrome(""))

# Not a palindrome
assert(is_palindrome("supercalifragilisticexpialidocious") == False)


