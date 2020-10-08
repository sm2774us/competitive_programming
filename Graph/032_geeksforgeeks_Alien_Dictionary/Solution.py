#
# Time  : O(N + K)
# Space : O(K)
# @tag : Graph ; DFS
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Alien Dictionary
#
# Description:
#
# Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.

# Note: Many orders may be possible for a particular test case, thus you may return any valid order.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N and k denoting the size of the dictionary. Then in the next line are sorted space separated values of the alien dictionary.
#
# Output:
# For each test case in a new line output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function findOrder() which takes the string array dict[], its size N and the integer K as inputs and returns a string denoting the order of characters in the alien language.
#
# Expected Time Complexity: O(N + K).
# Expected Auxiliary Space: O(K).
#
# Constraints:
# 1 <= T <= 1000
# 1 <= N <= 300
# 1 <= k <= 26
# 1 <= Length of words <= 50
#
# Example:
# Input:
# 2
# 5 4
# baa abcd abca cab cad
# 3 3
# caa aaa aab
#
# Output:
# 1
# 1
#
# Explanation:
# Test Case 1:
# Input:  Dict[ ] = { "baa", "abcd", "abca", "cab", "cad" }, k = 4
# Output: Function returns "bdac"
# Here order of characters is 'b', 'd', 'a', 'c'
# Note that words are sorted and in the given language "baa"
# comes before "abcd", therefore 'b' is before 'a' in output.
# Similarly we can find other orders.
#
# Test Case 2:
# Input: Dict[] = { "caa", "aaa", "aab" }, k = 3
# Output: Function returns "cab"
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/alien-dictionary/1 (GeeksForGeeks - Alien Dictionary)
#
# **************************************************************************
#
from typing import List
from collections import defaultdict

import unittest

# Python Program for Floyd Warshall Algorithm


class Solution:
    def dfs(self, d, v, visited, s):
        visited[v] = 1
        for i in d[v]:
            if visited[i] == 0:
                self.dfs(d, i, visited, s)
        s.append(chr(v + 97))

    def findOrder(self, l, n, k):
        visited = [0] * (26)
        visited1 = [0] * 26
        d = defaultdict(list)
        for i in range(0, n - 1, 1):
            k = l[i]
            k1 = l[i + 1]
            h = 0
            le1 = min(len(k), len(k1))
            while h < le1 and k[h] == k1[h]:
                h += 1
            if h < le1:
                d[ord(k[h]) - 97].append(ord(k1[h]) - 97)
        s = []
        st = ""
        for i in list(d):
            if d.get(i, 0) and visited[i] == 0:
                self.dfs(d, i, visited, s)
        s1 = ""
        if len(s) != k:
            # print("hello")
            for i in l:
                for j in i:
                    if visited[ord(j) - 97] == 0:
                        visited[ord(j) - 97] = 1
                        s1 += j
        return s1 + st.join(s[::-1])


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findOrderInAlienDictionary(self) -> None:
        sol = Solution()
        for l, n, k, solution in (
            [["baa", "abcd", "abca", "cab", "cad"], 5, 4, "bdac"],
            [["caa", "aaa", "aab"], 3, 3, "cab"],
        ):
            self.assertEqual(
                solution,
                sol.findOrder(l, n, k),
                "Should determine the order of characters in the alien language",
            )


# main
if __name__ == "__main__":
    unittest.main()
