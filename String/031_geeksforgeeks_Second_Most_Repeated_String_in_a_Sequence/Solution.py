#
# Time : O(N); Space: O(N)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Second most repeated string in a sequence
#
# Description:
#
# Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.
#
# Note: No two strings are the second most repeated, there will be always a single string.
#
# Example 1:
#
# Input:
# N = 6
# arr[] = {aaa, bbb, ccc, bbb, aaa, aaa}
# Output: bbb
# Explanation: "bbb" is the second most
# occurring string with frequency 2.
#
# â€‹Example 2:
#
# Input:
# N = 6
# arr[] = {geek, for, geek, for, geek, aaa}
# Output: for
# Explanation: "for" is the second most
# occurring string with frequency 2.
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function secFrequent() which takes the string array arr[] and its size N as inputs and returns the second most frequent string in the array.
#
#
# Expected Time Complexity: O(N*max(|Si|).
# Expected Auxiliary Space: O(N*max(|Si|).
#
#
# Constraints:
# 1<=N<=10^3
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence0534/1 (GeeksForGeeks - Second most repeated string in a sequence)
#
#
from typing import List
from collections import Counter

import unittest


class Solution:

    # Python 3 code to print Second most repeated
    # word in a sequence in Python
    #
    # Algorithm Description:
    # ------------------------
    # 1) Create a dictionary using Counter(iterator) method which contains words as keys and it’s frequency as value.
    # 2) Now get a list of all values in dictionary and sort it in descending order. Choose second element from the sorted list because it will be the second largest.
    # 3) Now traverse dictionary again and print key whose value is equal to second largest element.
    #
    def secondFrequent_solution_1(self, input: List[str]) -> str:

        # Convert given list into dictionary
        # it's output will be like {'ccc':1,'aaa':3,'bbb':2}
        dict = Counter(input)

        # Get the list of all values and sort it in ascending order
        value = sorted(dict.values(), reverse=True)

        # Pick second largest element
        secondLarge = value[1]

        # Traverse dictionary and print key whose
        # value is equal to second large element
        for (key, val) in dict.items():
            if val == secondLarge:
                # print(key)
                return key

    # Don't use this solution in an interview
    def secondFrequent_solution_2(self, input: List[str]) -> str:
        # this sorts from most common to least common to least common
        c = Counter(input)

        # c.most_common()[1] prints ('bbb',2)
        # c.most_common()[1][0] prints output: bbb
        # print(c.most_common()[1][0])
        return c.most_common()[1][0]

    def secondFrequent_solution_3(self, input: List[str]) -> str:
        obj = {}
        for word in input:
            if word in list(obj.keys()):
                obj[word] += 1
            else:
                obj[word] = 1
        objSorted = sorted(obj.items(), key=lambda x: x[1], reverse=True)
        # print(objSorted[1][0])
        return objSorted[1][0]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_secondFrequent(self) -> None:
        sol = Solution()
        for input, solution in (
            [["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"], "bbb"],
            [["geek", "for", "geek", "for", "geek", "aaa"], "for"],
        ):
            self.assertEqual(solution, sol.secondFrequent_solution_1(input))
            self.assertEqual(solution, sol.secondFrequent_solution_2(input))
            self.assertEqual(solution, sol.secondFrequent_solution_3(input))


if __name__ == "__main__":
    unittest.main()
