#
# Time :
# Space:
#
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks For Geeks: Check if strings are rotations of each other or not
#
# Description:
#
# Given two strings s1 and s2. The task is to check if s2 is a rotated version of the string s1. The characters in the strings are in lowercase.
#
#
#
# Example 1:
#
# Input:
# geeksforgeeks
# forgeeksgeeks
# Output:
# 1
# Explanation: s1 is geeksforgeeks, s2 is
# forgeeksgeeks. Clearly, s2 is a rotated
# version of s1 as s2 can be obtained by
# left-rotating s1 by 5 units.
#
#
# Example 2:
#
# Input:
# mightandmagic
# andmagicmigth
# Output:
# 0
# Explanation: Here with any amount of
# rotation s2 can't be obtained by s1.
#
#
# Your Task:
# The task is to complete the function areRotations() which checks if the two strings are rotations of each other. The function returns true if string 1 can be obtained by rotating string 2, else it returns false.
#
#
#
# Expected Time Complexity: O(N).
# Expected Space Complexity: O(N).
# Note: N = |s1|.
#
#
#
# Constraints:
# 1 <= |s1|, |s2| <= 107
#
# **************************************************************************
# Source    : https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1 (GeeksForGeeks - Check if strings are rotations of each other or not)

#
import re

import unittest


class Solution:

    # Solution 1:
    #
    def is_rotation_solution_1(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s1 in 2 * s2

    # Solution 2:   Uses Boyer-Moore Algorithm.
    #               For Python 2.4 and earlier solution 2 will be quicker than solution 1.
    #               Since Python 2.5 s1 in s2 is optimised to use Boyer-Moore Algorithm so need to use solution 2.
    #               (The python string methods uses an optimized Boyer-Moore-Horspool).
    #
    def is_rotation_solution_2(elf, s1: str, s2: str) -> bool:
        return (
            len(s1) == len(s2) and re.compile(re.escape(s1)).search(2 * s2) is not None
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_is_rotation(self) -> None:
        s = Solution()
        for s1, s2, solution in (
            ["geeksforgeeks", "forgeeksgeeks", True],
            ["mightandmagic", "andmagicmigth", False],
        ):
            self.assertEqual(solution, s.is_rotation_solution_1(s1, s2))
            self.assertEqual(solution, s.is_rotation_solution_2(s1, s2))


if __name__ == "__main__":
    unittest.main()
