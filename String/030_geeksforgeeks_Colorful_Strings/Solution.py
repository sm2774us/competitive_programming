#
# Time : O(N); Space: O(N)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Colorful Strings
#
# Description:
#
# Find the count of all possible strings of size n.Each character of the string is either ‘R’, ‘B’ or ‘G’. In the final string there needs to be at least r number of ‘R’, at least b number of ‘B’ and at least g number of ‘G’ (such that r + g + b <= n).
#
# Example 1:
#
# Input: n = 4, r = 1, g = 1, b = 1
# Output: 36
# Explanation: No. of 'R' >= 1,
# No. of ‘G’ >= 1, No. of ‘B’ >= 1
# and (No. of ‘R’) + (No. of ‘B’)
# + (No. of ‘G’) = n then
# following cases are possible:
# 1. RBGR and its 12 permutation
# 2. RBGB and its 12 permutation
# 3. RBGG and its 12 permutation
# Hence answer is 36.
# Example 2:
#
# Input: n = 4, r = 2, g = 0, b = 1
# Output: 22
# Explanation: No. of 'R' >= 2,
# No. of ‘G’ >= 0, No. of ‘B’ >= 1
# and (No. of ‘R’) + (No. of ‘B’)
# + (No. of ‘G’) <= n then
# following cases are possible:
# 1. RRBR and its 4 permutation
# 2. RRBG and its 12 permutation
# 3. RRBB and its 6 permutation
# Hence answer is 22.
#
# Your Task:
# You dont need to read input or print anything. Complete the function possibleStrings() which takes n, r, g, b as input parameter and returns the count of number of all possible strings..
#
# Expected Time Complexity: O(n2)
# Expected Auxiliary Space: O(n)
#
# Constraints:
# 1<= n <=20
# 1<= r+b+g <=n
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/geek-and-its-colored-strings1355/1 (GeeksForGeeks - Colorful Strings)
#
#
import unittest


class Solution:

    # Python 3 program to count number of
    # possible strings with n characters.

    # Function to calculate number of strings

    # Algorithm Description:
    # -----------------------
    # 1) As R, B and G have to be included atleast for given no. of times. Remaining values = n -(r + b + g).
    # 2) Make all combinations for the remaining values.
    # 3) Consider each element one by one for the remaining values and sum up all the permuations.
    # 4) Return total no. of permutations of all the combinations.
    #
    def possibleStrings(self, n: int, r: int, b: int, g: int) -> int:

        # Store factorial of numbers up to n
        # for further computation
        fact = [0 for i in range(n + 1)]
        fact[0] = 1
        for i in range(1, n + 1, 1):
            fact[i] = fact[i - 1] * i

            # Find the remaining values to be added
        left = n - (r + g + b)
        sum = 0

        # Make all possible combinations of
        # R, B and G for the remaining value
        for i in range(0, left + 1, 1):
            for j in range(0, left - i + 1, 1):
                k = left - (i + j)

                # Compute permutation of each
                # combination one by one and add them.
                sum = sum + fact[n] / (fact[i + r] * fact[j + b] * fact[k + g])

                # Return total no. of
        # strings/permutation
        return sum


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_possibleStrings(self) -> None:
        sol = Solution()
        for n, r, b, g, solution in ([4, 1, 1, 1, 36], [4, 2, 1, 0, 22]):
            self.assertEqual(solution, sol.possibleStrings(n, r, b, g))


if __name__ == "__main__":
    unittest.main()
