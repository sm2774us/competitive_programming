#
# Time : O(N * log(A)) ;
#       where: 1) N is the length of the string.
#              2) A is the size of the alphabet.
# The size of the heap will be at-most A.
# But since we remove and add back elements such that at each iteration we only
# add one character to the result, there will be N * lg(A) calls.
# Since A is fixed, we can assume complexity to be O(N).
#
# **************************************************************************
# Time : O(N)
# Space: O(A)
# @tag : Heap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 767: Reorganize String
#
# Description:
#
# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"
# Output: ""
# Note:
#
# S will consist of lowercase letters and have length in range [1, 500].
#
# **************************************************************************
# Source: https://leetcode.com/problems/reorganize-string/ (Leetcode - Problem 767 - Reorganize String)
#         https://practice.geeksforgeeks.org/problems/rearrange-characters/0 (GeeksForGeeks - Rearrange characters)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# Reorganize String https://leetcode.com/problems/reorganize-string/description/
#
# Algorithm
#
#   1. Say most frequently occuring character (say c) has frequency max_freq.
#      Then arrange c leaving a space between consecutive c's. The remaining characters should be more than the number
#      of spaces for a valid arrangement. This means that max_freq + (max_freq-1) <= len(S). We can test this quickly
#      using Counter class from collections module and using the mostcommon(i) method which returns
#      a list i most frequent tuples.
#
#   2. Now we create an array called result to store the result. We add (freq*-1,char) tuples to a heap
#      (this is how we simulate a max-heap in Python using a min-heap. We then pick the most frequent element
#       and if that element is not the last element in the result, we add it to result, If it is the last element
#       of the result, then we pick the second most frequent element and add that to the result, and also add back
#       the most frequent element back to the heap. Note when we pop from the heap and utilize the character in the
#       result, we need to add it back to the heap if the frequency is not -1 (-1 means that only one instance of that
#       element was in the heap and we have now used it, so no need to add it back).
#
# **************************************************************************
# Complexity Analysis:
# **************************************************************************
#   1. Time Complexity is O(N * lg(A)). N is the length of the string. A is the size of the alphabet. The size of the heap will be at-most A. But since we remove and add back elements such that at each iteration we only add one character to the result, there will be N * lg(A) calls. Since A is fixed, we can assume complexity to be O(N).
#   2. Space is also O(A).
# **************************************************************************
#
#
from collections import Counter
from heapq import heappush, heappop, heapify

import unittest


class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        :type S: str
        :rtype: str
        """
        max_freq = Counter(S).most_common(1)[0][1]
        if 2 * max_freq - 1 > len(S):
            return ""
        else:
            counter = Counter(S)
            heap = [(-value, key) for key, value in counter.items()]
            heapify(heap)

            result = []
            while heap:
                v, k = heappop(heap)
                if not result or k != result[-1]:  # can add the top most element
                    result.append(k)
                    if v != -1:
                        heappush(heap, (v + 1, k))
                else:  # cannot add the top most element
                    v1, k1 = heappop(heap)
                    result.append(k1)
                    heappush(heap, (v, k))
                    if v1 != -1:
                        heappush(heap, (v1 + 1, k1))
            return "".join(result)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reorganizeString(self) -> None:
        s = Solution()
        self.assertEqual("aba", s.reorganizeString("aab"))
        self.assertEqual("", s.reorganizeString("aaab"))


if __name__ == "__main__":
    unittest.main()
