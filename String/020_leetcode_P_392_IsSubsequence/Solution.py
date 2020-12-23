# Time  :
# Space :
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 392: Is Subsequence
#
# Description:
#
# Given a string s and a string t, check if s is subsequence of t.
#
# A subsequence of a string is a new string which is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
# and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# Both strings consists only of lowercase characters.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/is-subsequence/ (LeetCode - Problem 392 - Is Subsequence)
#
#
from collections import defaultdict
from bisect import bisect_left

import unittest


class Solution:

    # Solution 1: Two Pointers
    #
    # Each point in time we need to keep only two pointers: one for string s and one for string t.
    # Then if we find a new symbol in string t, which is equal to symbol in s, we move two pointers by one.
    # Otherwise, we move only pointer for t.
    #
    # Complexity is now only O(n + m) = O(n), because we traverse both strings only once.
    #
    # Time: O(n) ; Space: O(1)
    def isSubsequence_solution_1_using_two_pointers(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_i, t_i = 0, 0

        while s_i < len(s) and t_i < len(t):
            s_i, t_i = s_i + (s[s_i] == t[t_i]), t_i + 1

        return s_i == len(s)

    # Solution 2: Testing whether all characters in s are also in t (in order)
    #
    # This code is super short/fast but so hard to understand as a new python programmer.
    # Here is an explanation for other Python newbies:
    #
    # First, we turned t into a iterator, and what that does is that "c in it"
    # iterates through the iterator until the first position where it finds a match. See here.
    #
    # Second, (c in it for c in s) is a generator: it returns an iterator. More about generator here.
    #
    # Third, all() has only 1 parenthesis, so syntactic sugar: no need for double parentheses
    # all() takes in an iterator as an argument and loops through to find the first False.
    # If it can't find it, it return True. More about all/any and generator here.
    #
    # Below is the simulation of what the above function is doing under the hood:
    #
    # class Solution:
    #     def isSubsequence(self, s: str, t: str) -> bool:
    #         start=0
    #         for c in s:
    #             for i in range(start, len(t)):
    #                 if c==t[i]:
    #                     start=i+1
    #                     break
    #             else:
    #                 return False
    #         return True
    #
    # Time: O(|s| + |t|) ; Space: O(1)
    def isSubsequence_solution_2_concise(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)


# If you wanted to do the follow up properly (for an interview maybe)
#
# So we don't have to create the map every time isSubsequence is run.
# Note: this won't solve the current question because I've changed the function definition.
#
# Straight Forward Solution ( presented above ) will have:
# time complexity O(k*len(t)) and space O(1)
# for the follow-up.
#
# This solution trades memory for speed
# TC: O(log(len(t)) * sum(len(Sk)) + len(t))
# SC: O(len(t))

# To make time complexity analysis to be a lot neater for the follow up:
# Let Len of S be |S| and Len of T be |T|
#
# Step-1
# The pre-processing time in worst case could be O(T);// Assuming list is implemented using array or its like 2D array or matrix ==> its storage is O(1) operation
# ==> Step 1 time complexity= O(T)
#
# Step-2
# I am iterating through all the characters of S string // O(S) complexity
# For each character I am searching that in corresponding character array==> which is a sorted array of indexes using Binary Search ==> Log(T)
# ==> Step 2 time complexity= O(S * log(T))
#
# Total TC is Step 1 + Step 2
#
# ==> O(T) + O(S*log(T))
#
# Assuming S is far far smaller than T and could be ignored in comparison to T
#
# ==> O(T)
#
# ==> Let there be Q Queries
# ==> Total time Complexity = Q * O(T)
# ==> Total space Complexity = O(T)
#
#
# So, we get the following comparitive analysis:
#
# The straightforward solution in other threads would have time complexity O(k*len(t)) and space O(1)
# [ TC = O(K*T) ; SC = O(1) ]
# for the follow-up question.
#
# This one (with preprocessed t) has time complexity O(log(len(t)) * sum(len(Sk)) + len(t))
# [ assuming s is far smaller than t => TC = O(T) ]
# and space complexity O(len(t)). This solution trades memory for speed.
# [ SC = O(T) ]
#
# So, essentially this solution trades memory for speed
#
class FollowupSolution:
    def __init__(self, t: str) -> None:
        # create a map. key is char. value is index of apperance in acending order.
        self.posMap = defaultdict(list)
        for i, char in enumerate(t):
            self.posMap[char].append(i)

    # the 't' string is already chosen, so only pass in s
    def isSubsequence_follow_up_solution(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # lowBound is the minimum index the current char has to be at.
        lowBound = 0
        for char in s:
            if char not in self.posMap:
                return False
            charIndexList = self.posMap[char]
            # try to find an index that is larger than or equal to lowBound
            i = bisect_left(charIndexList, lowBound)
            if i == len(charIndexList):
                return False
            lowBound = charIndexList[i] + 1
        return True


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isSubsequence(self) -> None:
        sol = Solution()
        for s, t, solution in (["abc", "ahbgdc", True], ["axc", "ahbgdc", False]):
            self.assertEqual(
                solution, sol.isSubsequence_solution_1_using_two_pointers(s, t)
            )
            self.assertEqual(solution, sol.isSubsequence_solution_2_concise(s, t))

    def test_isSubsequence(self) -> None:
        t = "ahbgdc"
        sol = FollowupSolution(t)
        for s, solution in (["abc", True], ["axc", False]):
            self.assertEqual(solution, sol.isSubsequence_follow_up_solution(s))


if __name__ == "__main__":
    unittest.main()
