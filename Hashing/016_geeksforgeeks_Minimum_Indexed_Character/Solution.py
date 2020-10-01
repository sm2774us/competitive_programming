#
# Time : O(N); Space: O(N)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Minimum indexed character
#
# Description:
#
# Given a string str and another string patt. Find the character in patt that is present at the minimum index in str. If no character of patt is present in str then print ‘No character present’.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then the description of T test cases follow. Each test case contains two strings str and patt respectively.
#
# Output:
# Output the character in patt that is present at the minimum index in str. Print "$" (without quotes) if no character of patt is present in str.
#
# Constraints:
# 1 <= T <= 105
# 1 <= |str|, |patt| <= 105
#
# Example:
# Input:
# 2
# geeksforgeeks
# set
# adcffaet
# onkl
#
# Output:
# e
# $
#
# Explanation:
# Testcase 1: e is the character which is present in given patt "geeksforgeeks" and is first found in str "set".
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/minimum-indexed-character/0 (GeeksForGeeks - Minimum indexed character)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
import sys

import unittest

class Solution:
    # Function to find the
    # minimum index character
    def printMinIndexChar(self, str1: str, patt: str) -> str:

        # unordered_map 'um'
        # implemented as hash table
        um = {}

        # to store the index of
        # character having minimum index
        minIndex = sys.maxsize

        # Lengths of the two strings
        m = len(str1)
        n = len(patt)

        # Store the first index of
        # each character of 'str'
        for i in range(m):
            if (str1[i] not in um):
                um[str1[i]] = i

        # traverse the string 'patt'
        for i in range(n):

            # If patt[i] is found in 'um',
            # check if  it has the minimum
            # index or not accordingly
            # update 'minIndex'
            if (patt[i] in um and
                    um[patt[i]] < minIndex):
                minIndex = um[patt[i]]

        # Print the minimum index character
        if (minIndex != sys.maxsize):
            return str1[minIndex]

        # If no character of 'patt'
        # is present in 'str'
        else:
            return ""

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_printMinIndexChar(self) -> None:
        s = Solution()
        for str1, patt, solution in (
            ["geeksforgeeks", "set", "e"],
            ["adcffaet", "onkl", ""]
        ):
            self.assertEqual(
                solution,
                s.printMinIndexChar(str1, patt),
                "Should return the minimum indexed character"
            )


if __name__ == "__main__":
    unittest.main()
