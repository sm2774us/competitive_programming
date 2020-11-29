#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 93: Restore IP Addresses
#
# Description:
#
# Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
#
# A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
#
# Example 1:
#
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:
#
# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:
#
# Input: s = "1111"
# Output: ["1.1.1.1"]
# Example 4:
#
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]
# Example 5:
#
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
# Constraints:
#   * 0 <= s.length <= 3000
#   * s consists of digits only.

# **************************************************************************
# Source: https://leetcode.com/problems/restore-ip-addresses/ (LeetCode - Problem 93 - Restore IP Addresses)
#         https://practice.geeksforgeeks.org/problems/generate-ip-addresses/1 (GeeksForGeeks - Generate IP Addresses)
# **************************************************************************
#
from typing import List
import collections

import unittest


class Solution(object):
    def dfs_solution_1(self, s, idx, path, res):
        if idx > 4:
            return
        if idx == 4 and not s:
            res.append(path[:-1])
            return
        for i in range(1, len(s) + 1):
            if s[:i] == "0" or (s[0] != "0" and 0 < int(s[:i]) < 256):
                self.dfs_solution_1(s[i:], idx + 1, path + s[:i] + ".", res)

    def restoreIpAddresses_solution_1(self, s):
        res = []
        self.dfs_solution_1(s, 0, "", res)
        return res

    def dfs_solution_2(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return  # backtracking
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs_solution_2(s[i:], index + 1, path + s[:i] + ".", res)
                if s[0] == "0":  # here should be careful
                    break

    def restoreIpAddresses_solution_2(self, s):
        res = []
        self.dfs_solution_2(s, 0, "", res)
        return res

    # def restoreIpAddresses_solution_3(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #
    #     def valid(segment):
    #         """
    #         Check if the current segment is valid :
    #         1. less or equal to 255
    #         2. the first character could be '0'
    #            only if the segment is equal to '0'
    #         """
    #         return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
    #
    #     def update_output(curr_pos):
    #         """
    #         Append the current list of segments
    #         to the list of solutions
    #         """
    #         segment = s[curr_pos + 1:n]
    #         if valid(segment):
    #             segments.append(segment)
    #             output.append('.'.join(segments))
    #             segments.pop()
    #
    #     def backtrack(prev_pos=-1, dots=3):
    #         """
    #         prev_pos : the position of the previously placed dot
    #         dots : number of dots to place
    #         """
    #         # The current dot curr_pos could be placed
    #         # in a range from prev_pos + 1 to prev_pos + 4.
    #         # The dot couldn't be placed
    #         # after the last character in the string.
    #         for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
    #             segment = s[prev_pos + 1:curr_pos + 1]
    #             if valid(segment):
    #                 segments.append(segment)  # place dot
    #                 if dots - 1 == 0:  # if all 3 dots are placed
    #                     update_output(curr_pos)  # add the solution to output
    #                 else:
    #                     backtrack(curr_pos, dots - 1)  # continue to place dots
    #                 segments.pop()  # remove the last placed dot <---  BACKTRACKING
    #
    #     n = len(s)
    #     output, segments = [], []
    #     backtrack()


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_restoreIpAddresses(self) -> None:
        sol = Solution()
        for str, solution in (
            ["25525511135", ["255.255.11.135", "255.255.111.35"]],
            ["0000", ["0.0.0.0"]],
            ["1111", ["1.1.1.1"]],
            ["010010", ["0.10.0.10", "0.100.1.0"]],
            ["11211", ["1.1.2.11", "1.1.21.1", "1.12.1.1", "11.2.1.1"]],
        ):
            self.assertEqual(solution, sol.restoreIpAddresses_solution_1(str))
            self.assertEqual(solution, sol.restoreIpAddresses_solution_2(str))
            # self.assertEqual(solution, sol.restoreIpAddresses_solution_3(str))


# main
if __name__ == "__main__":
    unittest.main()
