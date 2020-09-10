# Time : O(|S|); Space: O(|S|) [|S| = absolute length of the string S]
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 8: String to Integer (atoi)
#
# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:
#
# Input: "42"
# Output: 42
# Example 2:
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:
#
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/string-to-integer-atoi/ (Leetcode - Problem 8 - String to Integer - atoi)
# Variant   : https://practice.geeksforgeeks.org/problems/implement-atoi/1 (GeeksForGeeks - Implement Atoi)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# 1) Here is my solution with a process to follow during a coding interview:
#
# Problem Summary / Clarifications / TDD:
# - Q1. What if there is a space between the sign and the number? (see cases 5 and 6)
# - Q2. What if the result is not an int. Python manages overflow issues. See case 12 and 14.
#
# Case.01. myAtoi("           ") = 0          (a non valid number with spaces only)
# Case.02. myAtoi("words      ") = 0          (a non valid number only)
# Case.03. myAtoi("words12365 ") = 0          (a non valid number is followed by a valid number I)
# Case.04. myAtoi("words 1236 ") = 0          (a non valid number is followed by a valid number II)
# Case.05. myAtoi("+ 4193"     ) = 0          (a non valid number: space between sign and number I)
# Case.06. myAtoi("- 4193    " ) = 0          (a non valid number: space between sign and number II)
#
# Case.07. myAtoi("4193"       ) = 4193       (a valid number only)
# Case.08. myAtoi("4193word"   ) = 4193       (a valid number is followed by a non valid number I)
# Case.09. myAtoi("4193 word"  ) = 4193       (a valid number is followed by a non valid number II)
# Case.10. myAtoi("4193 12 wo" ) = 4193       (a valid number is followed by a another valid number)
# Case.11. myAtoi("+4193"      ) = 4193       (a positive valid number with the sign +)
# Case.12. myAtoi("+2147483648") = 2147483647 (a positive number greater than int max value)
# Case.13. myAtoi("-4193"      ) = -4193      (a negatve valid number with the sign -)
# Case.14. myAtoi("-2147483649") = -2147483648(a negative number less than int min value)
#
# 2) Intuition:
# 2.1. Extract the number (str_num) from s
# 2.2. Extract the sign from str_num
# 2.3. Loop each digit of str_num and compute the conversion in num
# 2.4. Break when a non digit char is found or num reach max/min int
# 2.5. Return num * sign
#
# 3) Implementation: see below
#
# 4) Tests: Use all tests created in step 1 (TDD)
#
# 5) Complexity Analysis:
# **************************************************************************
# <> Time Complexity: O(|s|)
# <> Space Complexity: O(|s|)
# <> Could we do better?
#      * Time Complexity: We can't in term of asymptotic analysis but if we don't use the split function
#                         and break as soon as a non valid digit is found, the code may be faster.
#      * Space Complexity: Yes, we could make it O(1) if we don't use the split function and we loop on
#                          each character of s.
#
#
from typing import List
import collections

import unittest


class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0

        str = str.lstrip()
        if not str:
            return 0

        str_list = str.split()
        if not str_list:
            return 0

        num_str = str_list[0]
        sign = -1 if num_str[0] == "-" else +1
        start = 1 if num_str[0] in "-+" else 0

        num = 0
        # 0x80000000 => INT_MIN ; (-2**31) 2147483648
        # to
        # 0x7fffffff => INT_MAX ; (2**31 - 1) 2147483647
        int_boundary = 0x80000000 if sign == -1 else 0x7FFFFFFF

        for i in range(start, len(num_str)):
            ord_digit = ord(num_str[i])
            if ord_digit < 48 or ord_digit > 57:
                break

            num *= 10
            num += ord_digit - 48

            if num >= int_boundary:
                num = int_boundary
                break

        return num * sign

    def isNumericChar(self, x: str) -> bool:
        if x >= "0" and x <= "9":
            return True
        return False

    def myAtoiGeeksForGeeksIterative(self, str: str) -> int:
        if not str:
            return -1

        str = str.lstrip()
        if not str:
            return -1

        res = 0
        # initialize sign as positive
        sign = 1
        i = 0

        # if number is negative then update sign
        if str[0] == "-":
            sign = -1
            i += 1

        # Iterate through all characters of input string and update result
        for j in range(i, len(str)):
            # You may add some lines to write error message to error stream
            if self.isNumericChar(str[j]) == False:
                return -1

            res = res * 10 + (ord(str[j]) - ord("0"))

        return sign * res

    # # Recursive function to compute atoi()
    # def myAtoiGeeksForGeeksRecursive(self, str: str, num: int = 0) -> int:
    #     if not str: return -1
    #
    #     str = str.lstrip()
    #     if not str: return -1
    #
    #     # base case, we've hit the end of the string,
    #     # we just return the last value
    #     if len(str) == 1:
    #         return int(str) + (num * 10)
    #
    #     # add the next string item into our num value
    #     num = int(str[0:1]) + (num * 10)
    #
    #     # recurse through the rest of the string
    #     # and add each letter to num
    #     return self.myAtoiGeeksForGeeksRecursive(str[1:], num)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_myAtoiLeetcode(self) -> None:
        sol = Solution()
        for s, solution in (
            ["           ", 0],  # (a non valid number with spaces only)
            ["words      ", 0],  # (a non valid number only)
            ["words12365 ", 0],  # (a non valid number is followed by a valid number I)
            ["words 1236 ", 0],  # (a non valid number is followed by a valid number II)
            ["+ 4193", 0],  # (a non valid number: space between sign and number I)
            ["- 4193    ", 0],  # (a non valid number: space between sign and number II)
            ["4193", 4193],  # (a valid number only)
            ["4193word", 4193],  # (a valid number is followed by a non valid number I)
            [
                "4193 word",
                4193,
            ],  # (a valid number is followed by a non valid number II)
            [
                "4193 12 wo",
                4193,
            ],  # (a valid number is followed by a another valid number)
            ["+4193", 4193],  # (a positive valid number with the sign +)
            [
                "+2147483648",
                2147483647,
            ],  # (a positive number greater than int max value)
            ["-4193", -4193],  # (a negatve valid number with the sign -)
            ["-2147483649", -2147483648],  # (a negative number less than int min value)
            ["42", 42],
            ["   -42", -42],
            ["4193 with words", 4193],
            ["words and 987", 0],
            ["-91283472332", -2147483648],
        ):

            self.assertEqual(
                solution, sol.myAtoi(s), "Should convert the string to an integer"
            )

    def test_myAtoiGeeksForGeeks(self) -> None:
        sol = Solution()
        for s, solution in (["123", 123], ["21a", -1]):
            self.assertEqual(
                solution,
                sol.myAtoiGeeksForGeeksIterative(s),
                "Should convert the string to an integer",
            )
            # self.assertEqual(
            #     solution,
            #     sol.myAtoiGeeksForGeeksRecursive(s),
            #     "Should convert the string to an integer",
            # )


if __name__ == "__main__":
    unittest.main()
