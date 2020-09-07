#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Last index of One
#
# Given a string S consisting only '0's and '1's,  print the last index of the '1' present in it.
#
# Example 1:
#
# Input: "00001"
# Output: 4
#
# Example 2:
#
# Input: "0"
# Output: -1
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/last-index-of-1/0 (GeeksForGeeks - Last index of One)
#
# Solution: https://www.geeksforgeeks.org/find-last-index-character-string/
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# (Efficient : Traverse from right) :
# In above method 1, we always traverse complete string.
# In this method, we can avoid complete traversal in all those cases when x is present.
# The idea is to traverse from right side and stop as soon as we find character.
#
#
import unittest

class Solution:
    def findLastIndex(self, str: str) -> int:
        pattern = "1"
        # Traverse from right
        for i in range(len(str) - 1, -1, -1):
            if (str[i] == pattern):
                return i

        return -1

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findLastIndex(self) -> None:
        s = Solution()
        for str, solution in (
                ["00001", 4],
                ["4", -1]
        ):
            self.assertEqual(solution, s.findLastIndex(str), "Should return the last index of the '1' present in the given string")


if __name__ == '__main__':
    unittest.main()
