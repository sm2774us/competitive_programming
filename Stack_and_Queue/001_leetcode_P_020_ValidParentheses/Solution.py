#
# Time : O(N); Space: O(1)
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 20: Valid Parentheses
#
# Description:
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
#
# Input: s = "(]"
# Output: false
#
# Example 4:
#
# Input: s = "([)]"
# Output: false
#
# Example 5:
#
# Input: s = "{[]}"
# Output: true
#
# Constraints:
#   * 1 <= s.length <= 104
#   * s consists of parentheses only '()[]{}'.
#
# **************************************************************************
# Source: https://leetcode.com/problems/valid-parentheses/ (Leetcode - Problem 20 - Valid Parentheses)
#         https://practice.geeksforgeeks.org/problems/parenthesis-checker/0 (GeeksForGeeks - Parenthesis Checker)
#
#
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        opened = "({["
        closed = ")}]"
        d = dict(zip(opened, closed))
        # d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in opened:  # 1
                # if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0  # 3


# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isValid(self) -> None:
        s = Solution()
        for str, solution in (
            ["()", True],
            ["()[]{}", True],
            ["(]", False],
            ["([)]", False],
            ["{[]}", True],
        ):
            self.assertEqual(
                solution,
                s.isValid(str),
                "Should return if string has valid parentheses",
            )


if __name__ == "__main__":
    unittest.main()
