#
# Time  :
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Maximize Toys
#
# Description:
#
# Given an array arr of length N consisting cost of toys. Given an integer K depicting the amount with you. The task is to Maximise the number of different toys you can have with K amount.
#
# Example 1:
#
# Input: N = 7, K = 50
# arr = {1, 12, 5, 111, 200, 1000, 10}
# Output: 4
# Explaination: The costs of the toys are
# 1, 12, 5, 10.
# Example 2:
#
# Input: N = 3, K = 100
# arr = {20, 30, 50}
# Output: 3
# Explaination: We can buy all types of
# toys.
# Your Task:
# You do not need to read input or print anything. Your task is to complete the function toyCount() which takes the value N, K and the array arr and returns the maximum count of toys.
#
# Expected Time Complexity: O(NlogN)
# Expected Auxiliary Space: O(1)
#
# Constraints:
# 1 ≤ N ≤ 1000
# 1 ≤ K, arr[i] ≤ 10000
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/maximize-toys0331/1 (GeeksForGeeks - Maximize Toys)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import unittest

# Python 3 program to find
# the largest number that
# can be formed from given
# sum of digits and number
# of digits.
class Solution:
    # Prints the smalles
    # possible number with digit
    # sum 's' and 'm' number of
    # digits.
    def findLargest(self, N: int, S: int) -> int:

        # If sum of digits is 0,
        # then a number is possible
        # only if number of digits
        # is 1.
        if (S == 0):
            # if (N == 1):
            #     print("Largest number is ", "0", end="")
            # else:
            #     print("Not possible", end="")
            return None

        # Sum greater than the
        # maximum possible sum.
        if (S > 9 * N):
            # print("Not possible", end="")
            return None

        # Create an array to
        # store digits of
        # result
        res = [0] * N

        # Fill from most significant
        # digit to least significant
        # digit.
        for i in range(0, N):

            # Fill 9 first to make
            # the number largest
            if (S >= 9):
                res[i] = 9
                S = S - 9

            # If remaining sum
            # becomes less than
            # 9, then fill the
            # remaining sum
            else:
                res[i] = S
                S = 0

        # print("Largest number is ", end="")

        largest_number = []
        for i in range(0, N):
            largest_number.append(res[i])
            # print(res[i], end="")
        return int("".join(map(str, largest_number)))
    
class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findLargest(self) -> None:
        sol = Solution()
        for N, S, solution in (
            [2, 9, 90],
            [3, 20, 992]
        ):
            self.assertEqual(solution, sol.findLargest(N, S))


# main
if __name__ == "__main__":
    # # Driver code
    # sol = Solution()
    # N = 2
    # S = 9
    # sol.findLargest(N, S)
    unittest.main()
