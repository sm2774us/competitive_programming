# Time : O(N); Space: O(N), where n = S.length().
# @tag : String, Stack, Two Pointers, Recursion
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 1047: Remove All Adjacent Duplicates In String
#
# Description:
#
# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters,
# and removing them.
#
# We repeatedly make duplicate removals on S until we no longer can.
#
# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
#
# Example 1:
#
# Input: "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this
# is the only possible move.  The result of this move is that the string is "aaca", of which only "aa"
# is possible, so the final string is "ca".
#
#
# Note:
#
# 1 <= S.length <= 20000
# S consists only of English lowercase letters.
#
# **************************************************************************
# Source: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/ (Leetcode - Problem 1047 - Remove All Adjacent Duplicates In String)
#         https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates/0 (GeeksForGeeks - Recursively remove all adjacent duplicates)
#
# Solution Explanation
# **************************************************************************
# 1) Solution 1: Stack Based Solution
# **************************************************************************
# Keep a res as a characters stack.
# Iterate characters of S one by one.
#
# If the next character is same as the last character in res,
# pop the last character from res.
# In this way, we remove a pair of adjacent duplicates characters.
#
# If the next character is different,
# we append it to the end of res.
#
# **************************************************************************
# 2) Solution 2: Two Pointers Solution
# **************************************************************************
# If current char is same as the end of non-adjacent-duplicate chars, decrease the counter end by 1;
# otherwise, copy the current char to its end.
#
# **************************************************************************
# 3) Solution 3: Recursion Solution
# **************************************************************************
# 1. Check the length of S.
# 2. Replace all double letters with an empty string.
# 3. Check the length of S.
#
# If the length of S changed in the for loop, then call removeDuplicates with the new S, otherwise return S.
#
# **************************************************************************
# 4) Solution 4: One-Liner Solution
# **************************************************************************
#
#
from functools import reduce

import unittest


class Solution:
    def removeDuplicatesUsingStack(self, S: str) -> str:
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)

    def removeDuplicatesUsingTwoPointers(self, S: str) -> str:
        end, a = -1, list(S)
        for c in a:
            if end >= 0 and a[end] == c:
                end -= 1
            else:
                end += 1
                a[end] = c
        return "".join(a[: end + 1])

    def removeDuplicatesUsingRecursion(self, S: str, length=0) -> str:
        for l in set(S):
            S = S.replace(2 * l, "")
        return S if length == len(S) else self.removeDuplicatesUsingRecursion(S, len(S))

    def removeDuplicatesOneLiner(self, S: str) -> str:
        return reduce(lambda s, c: s[:-1] if s[-1:] == c else s + c, S)

    def removeDuplicatesRecursivelyGeeksForGeeks(self, S: str) -> str:
        lst = []
        pre = ""
        for i, data in enumerate(S):
            if i == 0:
                if S[i] != S[i + 1]:
                    lst.append(S[i])
            elif i == len(S) - 1:
                if S[i - 1] != S[i]:
                    lst.append(S[i])
            elif S[i - 1] != S[i] and S[i] != S[i + 1]:
                lst.append(S[i])

        S = ""
        for i, data in enumerate(lst):
            S += data
        pre = ""
        flag = 0

        for data in S:
            if data == pre:
                flag = 1
                break

        return S


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_removeDuplicatesLeetCode(self) -> None:
        s = Solution()
        for S, solution in (["abbaca", "ca"], ["geeksforgeek", "gksforgk"]):
            self.assertEqual(
                solution,
                s.removeDuplicatesUsingStack(S),
                "Should return the string with all adjacent duplicates removed",
            )
            self.assertEqual(
                solution,
                s.removeDuplicatesUsingTwoPointers(S),
                "Should return the string with all adjacent duplicates removed",
            )
            self.assertEqual(
                solution,
                s.removeDuplicatesUsingRecursion(S),
                "Should return the string with all adjacent duplicates removed",
            )
            self.assertEqual(
                solution,
                s.removeDuplicatesOneLiner(S),
                "Should return the string with all adjacent duplicates removed",
            )

    def test_removeDuplicatesRecurivelyGeeksForGeeks(self) -> None:
        s = Solution()
        for S, solution in (["geeksforgeek", "gksforgk"], ["acaaabbbacdddd", "acac"]):
            self.assertEqual(
                solution,
                s.removeDuplicatesRecursivelyGeeksForGeeks(S),
                "Should return the string with all adjacent duplicates removed",
            )


if __name__ == "__main__":
    unittest.main()
