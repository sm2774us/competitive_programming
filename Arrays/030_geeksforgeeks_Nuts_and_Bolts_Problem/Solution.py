#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Nuts and Bolts Problem
#
# Given a set of N nuts of different sizes and N bolts of different sizes. There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently.
#
# Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.
# The elements should follow the following order ! # $ % & * @ ^ ~ .
#
# Example 1:
#
# Input:
# N = 5
# nuts[] = {@, %, $, #, ^}
# bolts[] = {%, @, #, $ ^}
# Output:
# # $ % @ ^
# # $ % @ ^
# Example 2:
#
# Input:
# N = 9
# nuts[] = {^, &, %, @, #, *, $, ~, !}
# bolts[] = {~, #, @, %, &, *, $ ,^, !}
# Output:
# ! # $ % & * @ ^ ~
# ! # $ % & * @ ^ ~
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function matchPairs() which takes an array of characters nuts[], bolts[] and n as parameters and returns void. You need to change the array itswelf.
#
# Expected Time Complexity: O(NlogN)
# Expected Auxiliary Space: O(1)
#
# Constraints:
# 1 <= N <= 9
# Array of Nuts/Bolts can only consist of the following elements:{'@', '#', '$', '%', '^', '&', '~', '*', '!'}.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem0431/1 (GeeksForGeeks - Nuts and Bolts Problem)
#         Variant: https://www.lintcode.com/problem/nuts-bolts-problem/description (LintCode - Problem 399 - Nuts and Bolts Problem)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# **************************************************************************
# References:
# **************************************************************************
# https://www.geeksforgeeks.org/nuts-bolts-problem-lock-key-problem-set-2-hashmap/
# https://github.com/algorhythms/LintCode/blob/master/Nuts%20%26%20Bolts%20Problem.py
#
from typing import List
from collections import Counter

import unittest

# class Compare:
#     @classmethod
#     def cmp(cls, a, b):
#         """
#         THIS IS A SAMPLE CMP FOR TESTING.
#         You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
#         if "a" is bigger than "b", it will return 1, else if they are equal,
#         it will return 0, else if "a" is smaller than "b", it will return -1.
#         When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
#         :param a:
#         :param b:
#         :return:
#         """
#         a = a.lower()
#         b = b.lower()
#
#         diff = ord(a) - ord(b)
#         if diff < 0:
#             return -1
#         elif diff > 0:
#             return 1
#         else:
#             return 0


class Compare:
    @classmethod
    def cmp(cls, a, b):
        """
        THIS IS A SAMPLE CMP FOR TESTING.
        You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
        if "a" is bigger than "b", it will return 1, else if they are equal,
        it will return 0, else if "a" is smaller than "b", it will return -1.
        When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
        :param a:
        :param b:
        :return:
        """
        a = a.lower()
        b = b.lower()

        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0


class Solution(object):
    def matchPairs(self, nuts: List[str], bolts: List[str], n: int) -> List[str]:
        if not nuts or not bolts:
            return []
        if len(nuts) != len(bolts):
            return []

        allowed = ["!", "#", "$", "%", "&", "*", "@", "^", "~"]

        ans = []
        nuts_counter = Counter(nuts)
        bolts_counter = Counter(bolts)
        for i in allowed:
            if (i in nuts_counter) and (i in bolts_counter):
                ans.append(i)
        # print("matched nuts and bolts are-")
        # print(*ans)
        # print(*ans)
        return ans
        # hash1 = {}
        #
        # # creating a hashmap
        # # for nuts
        # for i in range(n):
        #     hash1[nuts[i]] = i
        #
        # # searching for nuts for
        # # each bolt in hash map
        # ans = []
        # for i in range(n):
        #     if (bolts[i] in hash1):
        #         nuts[i] = bolts[i]
        #         ans.append(nuts[i])
        #
        # # Print the result
        # print("matched nuts and bolts are-")
        # for i in range(n):
        #     print(nuts[i],
        #           end=" ")
        # print()
        # for i in range(n):
        #     print(bolts[i],
        #           end=" ")
        # return ans

    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts):
        """
        :param nuts: a list of nuts
        :param bolts: a list of bolts
        :return:
        """
        assert len(nuts) == len(bolts)
        self.quick_sort(nuts, bolts, 0, len(nuts))

    def quick_sort(self, nuts, bolts, start, end):
        """
        Quick sort over two arrays
        :param nuts:
        :param bolts:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return

        pivot = self.partition(nuts, bolts[start], start, end)
        self.partition(bolts, nuts[pivot], start, end)
        self.quick_sort(nuts, bolts, start, pivot)
        self.quick_sort(nuts, bolts, pivot + 1, end)

    def partition(self, A, pivot, start, end):
        """
        Use bolt to partition nuts/ Use nut to partition nuts
        Bolt and nut are swappable in the parameter
        In-place partition
        :param A: nuts or bolts, the counterpart of pivot
        :param pivot: bolt or nut
        :param start:
        :param end:
        :return: pivot
        """
        left = start  # save for the counterpart's pivot
        i = start + 1
        while i < end:
            if Compare.cmp(A[i], pivot) == -1 or Compare.cmp(pivot, A[i]) == 1:
                left += 1
                A[left], A[i] = A[i], A[left]
                i += 1
            elif Compare.cmp(A[i], pivot) == 0 or Compare.cmp(pivot, A[i]) == 0:
                A[start], A[i] = A[i], A[start]
            else:
                i += 1

        # move the counterpart's pivot from start to left
        A[start], A[left] = A[left], A[start]

        return left


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_matchPairs(self):
        s = Solution()
        for nuts, bolts, solution in (
            [
                ["@", "%", "$", "#", "^"],
                ["%", "@", "#", "$", "^"],
                ["#", "$", "%", "@", "^"],
            ],
            [
                ["^", "&", "%", "@", "#", "*", "$", "~", "!"],
                ["~", "#", "@", "%", "&", "*", "$", "^", "!"],
                ["!", "#", "$", "%", "&", "*", "@", "^", "~"],
            ],
        ):
            self.assertEqual(s.matchPairs(nuts, bolts, len(nuts)), solution)

    def test_sortNutsAndBolts(self):
        s = Solution()

        # nuts = ['a','b','d','g']
        # bolts = ['A','G','D','B']
        # s.sortNutsAndBolts(nuts, bolts)
        #
        # self.assertEqual(['a','b','d','g'], nuts)
        # self.assertEqual(['A','B','D','G'], bolts)

        nuts = ["ab", "bc", "dd", "gg"]
        bolts = ["AB", "GG", "DD", "BC"]
        s.sortNutsAndBolts(nuts, bolts)

        self.assertEqual(["ab", "bc", "dd", "gg"], nuts)
        self.assertEqual(["AB", "BC", "DD", "GG"], bolts)


if __name__ == "__main__":
    unittest.main()
