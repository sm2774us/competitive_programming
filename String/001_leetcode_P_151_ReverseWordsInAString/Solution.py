#
# Time : O(N); Space: O(N)
# @tag : String, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 151: Reverse Words In A String
#
# Description:
#
# Given an input string, reverse the string word by word.
#
# Example 1:
#
# Input: "the sky is blue"
# Output: "blue is sky the"
#
# Example 2:
#
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
#
# Example 3:
#
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#
# Example 4:
#
# Input: "i.like.this.program.very.much"
# Output: "much.very.program.this.like.i"
#
# Example 5:
#
# Input: "pqr.mno"
# Output: "mno.pqr"
#
# Note:
#
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.
#
# **************************************************************************
# Source: https://leetcode.com/problems/reverse-words-in-a-string/ (Leetcode - Problem 151 - Reverse Words in a String)
#         https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0 (GeeksForGeeks - Reverse words in a given string)
#
# Solution Explanation
# **************************************************************************
# Futher discussion: We can not do better than O(n) space in python, because strings are immutable.
#
# However if we are given not a string, but an array of symbols, we can remove all extra spaces, using Two pointers approach,
# reverse full string and then reverse each word. Time complexity will be O(n) and space will be O(1).
#
# Here is the python code:
#
# 1. We traverse chars with two pointers and rewrite symbols in the beginning.
# 2. Cut our chars, removing last elements (in my code it is not really inplace, but you can use del to do it in place)
# 3. Reverse list using chars.reverse().
# 4. Use two pointers to reverse each word.
from typing import Tuple

import unittest


class Solution:
    # # @param s, a string
    # # @param remove_chars, a Tuple of chars that can be construed as whitespace
    # # @param which, a string - takes the value of 'left'/'right'/'both'/'all' to remove relevant whitespace
    # # @return a string without whitespaces
    # def remove_whitespaces(self, s: str, remove_chars: Tuple[str] = (' ', '\n', '\t'), which: str = 'both') -> str:
    #     first_char = 0; last_char = 0
    #
    #     if which in ['left','both']:
    #         for idx,letter in enumerate(s):
    #             if not first_char and letter not in remove_chars:
    #                 first_char = idx
    #                 break
    #         if which == 'left':
    #             return s[first_char:]
    #
    #     if which in ['right','both']:
    #         for idx,letter in enumerate(s[::-1]):
    #             if not last_char and letter not in remove_chars:
    #                 last_char = -(idx + 1)
    #                 break
    #         return s[first_char:last_char+1]
    #
    #     if which == 'all':
    #         return ''.join([string for string in s if string not in remove_chars])

    # @param s, a string
    # @param delimiter, a delimiter
    # @return a string
    def reverseWordsWithDelimiterUsingBuiltIn(self, s: str, delimiter: str) -> str:
        return delimiter.join(s.strip().split(delimiter)[::-1])

    # @param s, a string
    # @param delimiter, a delimiter
    # @return a string
    def reverseWordsWithDelimiter(self, s: str, delimiter: str) -> str:
        chars = [t for t in s]
        slow, n = 0, len(s)
        for fast in range(n):
            if chars[fast] != delimiter or (
                fast > 0 and chars[fast] == delimiter and chars[fast - 1] != delimiter
            ):
                chars[slow] = chars[fast]
                slow += 1

        if slow == 0:
            return ""
        chars = chars[: slow - 1] if chars[-1] == delimiter else chars[:slow]
        chars.reverse()

        slow, m = 0, len(chars)
        for fast in range(m + 1):
            if fast == m or chars[fast] == delimiter:
                chars[slow:fast] = chars[slow:fast][::-1]
                # Reverse list, I again do it not in place, but you can easlily do it in place, as shown below:
                # chars.reverse()
                slow = fast + 1

        return "".join(chars)

    # @param s, a string
    # @return a string
    def reverseWordsUsingBuiltIn(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])

    # @param s, a string
    # @return a string
    def reverseWords(self, s: str) -> str:
        chars = [t for t in s]
        slow, n = 0, len(s)
        for fast in range(n):
            if chars[fast] != " " or (
                fast > 0 and chars[fast] == " " and chars[fast - 1] != " "
            ):
                chars[slow] = chars[fast]
                slow += 1

        if slow == 0:
            return ""
        chars = chars[: slow - 1] if chars[-1] == " " else chars[:slow]
        chars.reverse()

        slow, m = 0, len(chars)
        for fast in range(m + 1):
            if fast == m or chars[fast] == " ":
                chars[slow:fast] = chars[slow:fast][::-1]
                # Reverse list, I again do it not in place, but you can easlily do it in place, as shown below:
                # chars.reverse()
                slow = fast + 1

        return "".join(chars)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reverseWordsWithDelimiter(self) -> None:
        s = Solution()
        for str, delimiter, solution in (
            ["i.like.this.program.very.much", ".", "much.very.program.this.like.i"],
            ["pqr.mno", ".", "mno.pqr"],
        ):
            self.assertEqual(
                solution,
                s.reverseWordsWithDelimiterUsingBuiltIn(str, delimiter),
                "Should return the the string reversed word by word",
            )
            self.assertEqual(
                solution,
                s.reverseWordsWithDelimiter(str, delimiter),
                "Should return the the string reversed word by word",
            )

    def test_reverseWords(self) -> None:
        s = Solution()
        for str, solution in (
            ["the sky is blue", "blue is sky the"],
            ["  hello world!  ", "world! hello"],
            ["a good   example", "example good a"],
        ):
            self.assertEqual(
                solution,
                s.reverseWordsUsingBuiltIn(str),
                "Should return the the string reversed word by word",
            )
            self.assertEqual(
                solution,
                s.reverseWords(str),
                "Should return the the string reversed word by word",
            )


if __name__ == "__main__":
    unittest.main()
