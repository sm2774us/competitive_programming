#
# Time : O(N); Space: O(1)
# @tag : Recursion
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 651: 4 Keys Keyboard
#
# Description:
#
# Imagine you have a special keyboard with the following keys:
#
# Key 1: (A): Prints one 'A' on screen.
#
# Key 2: (Ctrl-A): Select the whole screen.
#
# Key 3: (Ctrl-C): Copy selection to buffer.
#
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
#
# Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A'
# you can print on screen.
#
# Example 1:
#
# Input: N = 3
# Output: 3
#
# Explanation:
# We can at most get 3 A's on screen by pressing following key sequence:
# A, A, A
#
# Example 2:
#
# Input: N = 7
# Output: 9
#
# Explanation:
# We can at most get 9 A's on screen by pressing following key sequence:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

# Note:
#   * 1 <= N <= 50
#   * Answers will be in the range of 32-bit signed integer.
#
# **************************************************************************
# Source: https://leetcode.com/articles/4-keys-keyboard (Leetcode - Problem 651 - 4 Keys Keyboard)
#         https://practice.geeksforgeeks.org/problems/special-keyboard3018/1 (GeeksForGeeks - Special Keyboard)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
#
import collections

import unittest


class Solution(object):
    def maxA(self, N: int) -> int:
        """
        :type N: int
        :rtype: int
        """
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        dp[0][0] = 0  # step, buffer
        for z in range(N):
            for y in dp[z]:
                # Key 1: (A):
                dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + 1)
                # Key 4: (Ctrl-V):
                dp[z + 1][y] = max(dp[z + 1][y], dp[z][y] + y)
                # Key 2: (Ctrl-A): + Key 3: (Ctrl-C):
                dp[z + 2][dp[z][y]] = max(dp[z + 2][dp[z][y]], dp[z][y])
        return max(dp[N].values())


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxA(self) -> None:
        sol = Solution()
        for N, solution in ([3, 3], [7, 9]):
            self.assertEqual(
                solution,
                sol.maxA(N),
                "Should return the maximum numbers of 'A' you can print on screen",
            )


if __name__ == "__main__":
    unittest.main()
