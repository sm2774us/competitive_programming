#
# Time  :
# Space :
# @tag  : Arrays
# @by   : Shaikat Majumdar
# @date : Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Jumping Caterpillars
#
# Given N leaves numbered from 1 to N . A caterpillar at leaf 1, jumps from leaf to leaf in multiples of Aj (Aj, 2Aj, 3Aj).
# j is specific to the caterpillar. Whenever a caterpillar reaches a leaf, it eats it a little bit.. You have to find out how many leaves, from 1 to N, are left uneaten after all K caterpillars have reached the end. Each caterpillar has its own jump factor denoted by Aj, and each caterpillar starts at leaf number 1.
#
# Input:
# The first line consists of a integer T denoting the number of testcases. T test cases follow. Each test case consists of two lines of input. The first line consists of two integers: N, which denotes the number of leaves; and K, which denotes the number of caterpillars. Second line of each test case consists of K space seperated integers denoting the jumping factor of caterpillars.
#
# Output:
# For each testcase, in a new line, print a  single integer denoting the number of uneaten leaves.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= K <= 107
# 1 <= Aj <= 100
#
# Example:
# Input:
# 1
# 10 3
# 2 3 5
# Output:
# 2
#
# Explanation:
# Testcase1: The leaves eaten by the first caterpillar are (2, 4, 6, 8, 10).
# The leaves eaten by the second caterpilllar are (3, 6, 9)
# The leaves eaten by the third caterpilllar are (5, 10)
# Ultimately, the uneaten leaves are 1, 7 and their number is 2
#
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/jumping-caterpillars/0 (GeeksForGeeks - Jumping Caterpillars)
#
# **************************************************************************
# Reference: https://nkimberly.wordpress.com/2018/08/06/exploring-the-caterpillar-problem/
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#

import unittest


class Solution:
    def leftover_leaves_1_nested_loops(self, num_leaves, caterpillar_jumps):
        eat_count = 0
        eaten = False
        for num_leaf in range(1, num_leaves + 1):
            for num_jump in caterpillar_jumps:
                if num_leaf % num_jump == 0:
                    eaten = True
                    break
            if eaten is True:
                eat_count += 1
            eaten = False
        leftover = num_leaves - eat_count
        return leftover

    def leftover_leaves_2_math(self, num_leaves, jumps):
        subsets = []
        n = len(jumps) - 1
        self.sub_pairs(jumps, 0, n, [], subsets)

        eaten = 0
        for num_jump in jumps:
            eaten += num_leaves // num_jump

        for subset in subsets:
            composite_lcm = self.find_lcm(subset[0], subset[1])
            for i in range(2, len(subset)):
                composite_lcm = self.find_lcm(composite_lcm, subset[i])
            if len(subset) % 2 == 0:
                eaten -= num_leaves // composite_lcm
            else:
                eaten += num_leaves // composite_lcm

        leftover = num_leaves - eaten
        return leftover

    def sub_pairs(self, arr, s, e, sub_arr, subsets):
        if s == e + 1:
            if len(sub_arr) > 1 and len(sub_arr) <= len(arr):
                subsets.append(sub_arr)
            return subsets
        self.sub_pairs(arr, s + 1, e, sub_arr, subsets)
        self.sub_pairs(arr, s + 1, e, sub_arr + [arr[s]], subsets)

    def find_lcm(self, num1, num2):
        if num1 > num2:
            num = num1
            den = num2
        else:
            num = num2
            den = num1
        rem = num % den
        while rem != 0:
            num = den
            den = rem
            rem = num % den
        gcd = den
        lcm = int(int(num1 * num2) / int(gcd))
        return lcm


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_leftover_leaves(self) -> None:
        s = Solution()
        for num_leaves, caterpillar_jumps, solution in (
            [10, [2, 3, 5], 2],
            [10, [2, 3], 3],
        ):
            self.assertEqual(
                solution,
                s.leftover_leaves_1_nested_loops(num_leaves, caterpillar_jumps),
            )
            self.assertEqual(
                solution, s.leftover_leaves_2_math(num_leaves, caterpillar_jumps)
            )


if __name__ == "__main__":
    unittest.main()
