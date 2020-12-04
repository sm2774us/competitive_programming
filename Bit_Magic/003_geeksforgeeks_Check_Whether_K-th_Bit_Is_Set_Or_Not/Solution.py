#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Check whether K-th bit is set or not
#
# Description:
#
# Given a number N and a bit number K, check if Kth bit of N is set or not. A bit is called set if it is 1. Position of set bit '1' should be indexed starting with 0 from LSB side in binary representation of the number.
# Example, Consider N = 4(100):  0th bit = 0, 1st bit = 0, 2nd bit = 1.
#
# Example 1:
#
# Input: N = 4, K = 0
# Output: false
# Explanation: Binary representation of 4 is 100,
# in which 0th bit from LSB is not set.
# So, return false.
# Example 2:
#
# Input: N = 4, K = 2
# Output: true
# Explanation: Binary representation of 4 is 100,
# in which 2nd bit from LSB is set.
# So, return true.
# Example 3:
#
# Input: N = 500, K = 3
# Output: false
# Explanation: Binary representation of 500 is
# 111110100, in which 3rd bit from LSB is not set.
# So, return false.
#
# Your Task:  This is a function problem. You only need to complete the function checkKthbit that takes n and k as parameters and returns either true (if kth bit is set) or false(if kth bit is not set).
#
# Expected Time Complexity: O(1).
# Expected Auxiliary Space: O(1).
#
# Constraints:
#   * 1 ≤ N ≤ 109
#   * 0 ≤ K ≤ floor(log2(N) + 1)
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1 (GeeksForGeeks - Rightmost different bit )
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Bit_Manipulation_Tricks_Part_4_Playing_With_K-th_Bit.md ( one level directory above )
#
# **************************************************************************
#
import unittest


class Solution(object):
    def checkKthBit(self, n: int, k: int) -> bool:
        return bool(n & (1 << k))
        # l = (bin(n)[2:][::-1])
        # if (l[k] == '1'):
        #     return True
        # else:
        #     return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_checkKthBit(self) -> None:
        sol = Solution()
        for n, k, solution in ([4, 0, False], [4, 2, True], [500, 3, False]):
            self.assertEqual(solution, sol.checkKthBit(n, k))


# main
if __name__ == "__main__":
    unittest.main()
