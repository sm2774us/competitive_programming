#
# Time : O(N); Space: O(N)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Check if frequencies can be equal
#
# Description:
#
# Given a string s which contains only lower alphabetic characters, check if it is possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string.
#
# Example 1:
#
# Input:
# s = xyyz
# Output: 1
# Explanation: Removing one 'y' will make
# frequency of each letter 1.
#
# Example 2:
#
# Input:
# s = xxxxyyzz
# Output: 0
# Explanation: Frequency can not be made same
# same by removing just 1 character.
#
# Your Task:
# You dont need to read input or print anything. Complete the function sameFreq() which takes a string as input parameter and returns a boolean value denoting if same frequency is possible or not.
# Note: The driver code print 1 if the value returned is true, otherwise 0.
#
#
# Expected Time Complexity: O(N) where N is length of str
# Expected Auxiliary Space: O(1)
#
#
# Constraints:
# 1 <= str.length() <= 104
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/check-frequencies4211/1 (GeeksForGeeks - Check if frequencies can be equal)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
from typing import List

import unittest

M = 26


class Solution:
    # Utility method to get index of character ch
    # in lower alphabet characters
    def getIdx(self, ch: str) -> int:
        return ord(ch) - ord("a")

        # Returns true if all non-zero elements

    # values are same
    def allSame(self, freq: List[int], N: int) -> bool:
        # get first non-zero element
        for i in range(0, N):
            if freq[i] > 0:
                same = freq[i]
                break

        # check equality of each element
        # with variable same
        for j in range(i + 1, N):
            if freq[j] > 0 and freq[j] != same:
                return False

        return True

    # Returns true if we can make all
    # character frequencies same
    def possibleSameCharFreqByOneRemoval(self, str1: str) -> bool:
        l = len(str1)

        # fill frequency array
        freq = [0] * M
        for i in range(0, l):
            freq[self.getIdx(str1[i])] += 1

        # if all frequencies are same,
        # then return true
        if self.allSame(freq, M):
            return True

        # Try decreasing frequency of all character
        # by one and then check all equality of all
        # non-zero frequencies
        for i in range(0, 26):

            # Check character only if it
            # occurs in str
            if freq[i] > 0:
                freq[i] -= 1

                if self.allSame(freq, M):
                    return True
                freq[i] += 1

        return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_printMinIndexChar(self) -> None:
        s = Solution()
        for str1, solution in (["xyyz", True], ["xxxxyyzz", False]):
            self.assertEqual(
                solution,
                s.possibleSameCharFreqByOneRemoval(str1),
                "Should determine if it is possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string",
            )


if __name__ == "__main__":
    unittest.main()
