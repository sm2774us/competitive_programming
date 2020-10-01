#  Google | OA 2019 | Interview Question | Compare Strings
#
# Time : O(N); Space: O(N)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# One string is strictly smaller than another when the frequency of occurrence of the smallest character in the
# string is less than the frequency of occurrence of the smallest character in the comparison string.
#
# For example, string "abcd" is smaller than string "aaa" because the smallest character (in lexicographical order)
# in "abcd" is 'a', with a frequency of 1, and the smallest character in "aaa" is also 'a', but with a frequency of 3.
# In another example, string "a" is smaller than string "bb" because the smallest character in "a" is 'a' with a
# frequency of 1, and the smallest character in "bb" is 'b' with a frequency of 2.
#
# Write a function that, given string A (which contains M strings delimited by ',') and string B (which contains N
# strings delimited by ','), returns an array C of N integers. For 0 <= J < N, values of C[J] specify the number of
# strings in A which are strictly smaller than the comparison J-th string in B (starting from 0).
#
# For example, given strings A and B such that:
# A = "abcd aabc bd"
# B = "aaa aa"
#
# The function should return [3, 2] because:
#
# All the strings in the array are strictly smaller than "aaa" on the basis of the given comparison criteria;
#
# Strings "abcd" and "bd" are strictly smaller than "aa".
#
# Assume that:
#   * 1 <= N, M <= 10000
#   * 1 <= length of any string contained by A or B <= 10
#   * All the input strings comprise only lowercase English alphabet letters (a-z)
#
# In your solution, focus on correctness. The performance of your solution will not be the primary focus of the
# assessment.
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/356960 (Google OA 2019 - Interview Question - Compare Strings)
#
# NOTE: Same as the leetcode problem:
#       Leetcode - Problem 1170 - Compare Strings by Frequency of the Smallest Character
# **************************************************************************
#       https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
# **************************************************************************
#
#
from typing import List

import unittest


class Solution:
    # Google | OA 2019 | Interview Question | Compare Strings | Solution
    def solve(self, A: str, B: str) -> List[int]:
        wordsA = A.split(",")
        wordsB = B.split(",")
        freqCounter = [0] * 10

        for w in wordsA:
            minFreq = w.count(min(w))
            freqCounter[minFreq] += 1

        toReturn = []
        for w in wordsB:
            minFreq = w.count(min(w))
            toReturn.append(sum(freqCounter[:minFreq]))

        return toReturn

    # Leetcode - Problem 1170 - Compare Strings by Frequency of the Smallest Character | Solution
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = lambda s: s.count(min(s))
        l, wlst = len(words), [f(word) for word in words]
        biggerthan, m = [0] * 11, [0] * 11
        for i in wlst:
            m[i] += 1
        # compute a list contain bigger than frequence occurence
        for i in range(1, 11):
            # the sum of frequence less or equal than i, prefix sum
            m[i] += m[i - 1]
            # the amount of frequence greater than i
            biggerthan[i] = l - m[i]
        return [biggerthan[f(i)] for i in queries]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_compareStringsGoogle_OA_2019(self) -> None:
        sol = Solution()
        self.assertEqual([3, 2], sol.solve("abcd,aabc,bd", "aaa,aa"))
        for A, B, solution in (
            ["abcd,aabc,bd", "aaa,aa", [3, 2]],
            ["abcd", "aaa", [1]],
            ["a", "bb", [1]],
        ):
            self.assertEqual(solution, sol.solve(A, B))

    def test_numSmallerByFrequencyLeetcode(self) -> None:
        sol = Solution()
        self.assertEqual([1], sol.numSmallerByFrequency(["cbd"], ["zaaaz"]))


if __name__ == "__main__":
    unittest.main()
