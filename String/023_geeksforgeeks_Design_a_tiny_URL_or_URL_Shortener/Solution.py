#
# Time :
# Space:
#
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks For Geeks: Design a tiny URL or URL shortener
#
# Description:
#
# Design a system that takes big URLs like “http://www.geeksforgeeks.org/count-sum-of-digits-in-numbers-from-1-to-n/” and converts them into a short URL. It is given that URLs are stored in database and every URL has an associated integer id.  So your program should take an integer id and generate a URL.
#
# A URL character can be one of the following
#
# A lower case alphabet [‘a’ to ‘z’], total 26 characters
# An upper case alphabet [‘A’ to ‘Z’], total 26 characters
# A digit [‘0′ to ‘9’], total 10 characters
# There are total 26 + 26 + 10 = 62 possible characters.
#
# So the task is to convert an integer (database id) to a base 62 number where digits of 62 base are "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
# OPQRSTUVWXYZ0123456789"
#
# Example 1:
#
# Input:
# N = 12345
# Output:
# dnh
# 12345
# Explanation: "dnh" is the url for id 12345
# Example 2:
#
# Input:
# N = 30540
# Output:
# h6K
# 30540
# Explanation: "h6K" is the url for id 30540
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function idToShortURL() which takes the integer n as parameters and returns an string denoting the answer.
#
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
#
# Constraints:
# 1 ≤ N ≤ 1018
#
# **************************************************************************
# Source    : https://practice.geeksforgeeks.org/problems/design-a-tiny-url-or-url-shortener2031/1 (GeeksForGeeks - Design a tiny URL or URL shortener)
#
# Reference: https://stackoverflow.com/a/1119769
#
import string
import unittest

BASE62 = string.ascii_letters + string.digits


class Solution:

    # There is no standard module for this, but I have written my own functions to achieve that
    #
    # Notice the fact that you can give it any alphabet to use for encoding and decoding.
    # If you leave the alphabet argument out, you are going to get the 62 character alphabet
    # defined on the first line of code, and hence encoding/decoding to/from 62 base.
    #
    def idToShortURL(self, num: int, alphabet: str = BASE62) -> str:
        """Encode a positive number into Base X and return the string.

        Arguments:
        - `num`: The number to encode
        - `alphabet`: The alphabet to use for encoding
        """
        if num == 0:
            return alphabet[0]
        arr = []
        arr_append = arr.append  # Extract bound-method for faster access.
        _divmod = divmod  # Access to locals is faster.
        base = len(alphabet)
        while num:
            num, rem = _divmod(num, base)
            arr_append(alphabet[rem])
        arr.reverse()
        return "".join(arr)

    def shortURLToId(self, string: str, alphabet: str = BASE62) -> int:
        """Decode a Base X encoded string into the number

        Arguments:
        - `string`: The encoded string
        - `alphabet`: The alphabet to use for decoding
        """
        base = len(alphabet)
        strlen = len(string)
        num = 0

        idx = 0
        for char in string:
            power = strlen - (idx + 1)
            num += alphabet.index(char) * (base ** power)
            idx += 1

        return num

    # # Python3 code for above approach
    # def idToShortURL(self, id: int) -> str:
    #     map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    #     shortURL = ""
    #
    #     # for each digit find the base 62
    #     while (id > 0):
    #         shortURL += map[id % 62]
    #         id //= 62
    #
    #     # reversing the shortURL
    #     return shortURL[len(shortURL):: -1]
    #
    # def shortURLToId(self, shortURL: str) -> int:
    #     id = 0
    #     for i in shortURL:
    #     #for i in shortURL[::-1]:
    #         val_i = ord(i)
    #         if (val_i >= ord('a') and val_i <= ord('z')):
    #             id = id * 62 + val_i - ord('a')
    #         elif (val_i >= ord('A') and val_i <= ord('Z')):
    #             id = id * 62 + val_i - ord('Z') + 26
    #         else:
    #             id = id * 62 + val_i - ord('0') + 52
    #     return id


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_idToShortURL(self) -> None:
        s = Solution()
        for id, shotURL in ([12345, "dnh"], [30540, "h6K"]):
            self.assertEqual(shotURL, s.idToShortURL(id))

    def test_shortURLToId(self) -> None:
        s = Solution()
        for shotURL, id in (["dnh", 12345], ["h6K", 30540]):
            self.assertEqual(id, s.shortURLToId(shotURL))

    # def test_idToShortURL(self) -> None:
    #     s = Solution()
    #     for id, shotURL in (
    #         [12345, "dnh"],
    #         [30540, "h6K"]
    #     ):
    #         self.assertEqual(shotURL, s.idToShortURL(id))
    #
    # def test_shortURLToId(self) -> None:
    #     s = Solution()
    #     for shotURL, id in (
    #         ["dnh", 12345],
    #         ["h6K", 30540]
    #     ):
    #         self.assertEqual(id, s.shortURLToId(shotURL))


if __name__ == "__main__":
    unittest.main()
