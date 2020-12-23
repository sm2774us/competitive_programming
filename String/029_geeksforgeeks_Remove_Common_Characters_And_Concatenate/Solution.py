#
# Time : O(N); Space: O(N)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Remove common characters and concatenate
#
# Description:
#
# Given two strings s1 and s2. Modify both the strings such that all the common characters of s1 and s2
# are to be removed and the uncommon characters of s1 and s2 are to be concatenated.
# Note: If all characters are removed print -1.
#
# Example 1:
#
# Input:
# s1 = aacdb
# s2 = gafd
# Output: cbgf
# Explanation: The common characters of s1
# and s2 are: a, d. The uncommon characters
# of s1 and s2 are c, b, g and f. Thus the
# modified string with uncommon characters
# concatenated is cbgf.
# Example 2:
#
# Input:
# s1 = abcs
# s2 = cxzca
# Output: bsxz
# Explanation: The common characters of s1
# and s2 are: a,c. The uncommon characters
# of s1 and s2 are b,s,x and z. Thus the
# modified string with uncommon characters
# concatenated is bsxz.
# Your Task:
# The task is to complete the function concatenatedString() which removes the common characters, concatenates,
# and returns the string. If all characters are removed then return -1.
#
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(Number of distinct characters).
# Note: N = |Length of Strings|
#
# Constraints:
# 1 <= |Length of Strings| <= 10^4
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/remove-common-characters-and-concatenate-1587115621/1 (GeeksForGeeks - Remove common characters and concatenate)
#
#
import unittest


class Solution:
    def concatst(self, str1: str, str2: str) -> str:
        st = ""
        for i in range(len(str1)):
            if str1[i] not in str2:
                st += str1[i]

        for i in range(len(str2)):
            if str2[i] not in str1:
                st += str2[i]
        if len(st) == 0:
            return "-1"
        else:
            return st


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_concatst(self) -> None:
        sol = Solution()
        for str1, str2, solution in (
            ["aacdb", "gafd", "cbgf"],
            ["abcs", "cxzca", "bsxz"],
        ):
            self.assertEqual(solution, sol.concatst(str1, str2))


if __name__ == "__main__":
    unittest.main()
