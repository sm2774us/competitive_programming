#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Count total set bits
#
# Description:
#
# You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).
#
# Example 1:
#
# Input: N = 4
# Output: 5
# Explanation:
# For numbers from 1 to 4.
# For 1: 0 0 1 = 1 set bits
# For 2: 0 1 0 = 1 set bits
# For 3: 0 1 1 = 2 set bits
# For 4: 1 0 0 = 1 set bits
# Therefore, the total set bits is 5.
# Example 2:
#
# Input: N = 17
# Output: 35
# Explanation: From numbers 1 to 17(both inclusive),
# the total number of set bits is 35.
#
# Your Task: The task is to complete the function countSetBits() that takes n as a parameter and returns the count of all bits.
#
# Expected Time Complexity: O(log N).
# Expected Auxiliary Space: O(1).
#
# Constraints:
# 1 ≤ N ≤ 106
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1 (GeeksForGeeks - Count total set bits)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import unittest


class Solution(object):

    # Solution 1: Simple
    #
    #             A simple solution is to run a loop from 1 to n and sum
    #             the count of set bits in all numbers from 1 to n.
    #
    # Time Complexity: O(NlogN)

    # A utility function to count set bits
    # in a number x
    def countSetBitsUtil(self, x):

        if x <= 0:
            return 0
        return (0 if int(x % 2) == 0 else 1) + self.countSetBitsUtil(int(x / 2))

    # Returns count of set bits present in
    # all numbers from 1 to n
    def countTotalSetBits_solution_1(self, n: int) -> int:
        # initialize the result
        bitCount = 0

        for i in range(1, n + 1):
            bitCount += self.countSetBitsUtil(i)

        return bitCount

    # Solution 2: More Efficient Approach than Solution 1
    #

    # Function which counts set bits from 0 to n
    def countTotalSetBits_solution_2(self, n: int) -> int:
        i = 0

        # ans store sum of set bits from 0 to n
        ans = 0

        # while n greater than equal to 2^i
        while (1 << i) <= n:

            # This k will get flipped after
            # 2^i iterations
            k = 0

            # change is iterator from 2^i to 1
            change = 1 << i

            # This will loop from 0 to n for
            # every bit position
            for j in range(0, n + 1):
                ans += k

                if change == 1:

                    #  When change = 1 flip the bit
                    k = not k

                    # again set change to 2^i
                    change = 1 << i

                else:
                    change -= 1

            # increment the position
            i += 1

        return ans

    # Solution 3: Tricky
    #

    # A O(Logn) complexity program to count
    # set bits in all numbers from 1 to n

    """ 
    /* Returns position of leftmost set bit. 
    The rightmost position is considered 
    as 0 */ 
    """

    def getLeftmostBit(self, n):

        m = 0
        while n > 1:
            n = n >> 1
            m += 1

        return m

    """ 
    /* Given the position of previous leftmost 
    set bit in n (or an upper bound on 
    leftmost position) returns the new 
    position of leftmost set bit in n */ 
    """

    def getNextLeftmostBit(self, n, m):

        temp = 1 << m
        while n < temp:
            temp = temp >> 1
            m -= 1

        return m

    def _countSetBits(self, n, m):

        # Base Case: if n is 0, then set bit
        # count is 0
        if n == 0:
            return 0

        # /* get position of next leftmost set bit */
        m = self.getNextLeftmostBit(n, m)

        # If n is of the form 2^x-1, i.e., if n
        # is like 1, 3, 7, 15, 31, .. etc,
        # then we are done.
        # Since positions are considered starting
        # from 0, 1 is added to m
        if n == (1 << (m + 1)) - 1:
            return (m + 1) * (1 << m)

        # update n for next recursive call
        n = n - (1 << m)
        return (n + 1) + self.countTotalSetBits_solution_3(n) + m * (1 << (m - 1))

    # The main recursive function used by countSetBits()
    # def _countSetBits(n, m)

    # Returns count of set bits present in
    # all numbers from 1 to n
    def countTotalSetBits_solution_3(self, n):

        # Get the position of leftmost set
        # bit in n. This will be used as an
        # upper bound for next set bit function
        m = self.getLeftmostBit(n)

        # Use the position
        return self._countSetBits(n, m)

    # Solution 4: Using Table Approach
    #

    # Time Complexity: O(LogN)

    # Returns count of set bits present in
    # all numbers from 1 to n
    def countTotalSetBits_solution_4(self, n):

        # Ignore 0 as all the bits are unset
        n += 1

        # To store the powers of 2
        powerOf2 = 2

        # To store the result, it is initialized
        # with n/2 because the count of set
        # least significant bits in the integers
        # from 1 to n is n/2
        cnt = n // 2

        # Loop for every bit required to represent n
        while powerOf2 <= n:

            # Total count of pairs of 0s and 1s
            totalPairs = n // powerOf2

            # totalPairs/2 gives the complete
            # count of the pairs of 1s
            # Multiplying it with the current power
            # of 2 will give the count of
            # 1s in the current bit
            cnt += (totalPairs // 2) * powerOf2

            # If the count of pairs was odd then
            # add the remaining 1s which could
            # not be grouped together
            if totalPairs & 1:
                cnt += n % powerOf2
            else:
                cnt += 0

            # Next power of 2
            powerOf2 <<= 1

        # Return the result
        return cnt

    # Solution 5: Dynamic Programming
    #

    # Time Complexity: O(LogN)

    # Returns count of set bits present in
    # all numbers from 1 to n
    def countTotalSetBits_solution_5(self, n):
        # To store the required count
        # of the set bits
        cnt = 0

        # To store the count of set
        # bits in every integer
        setBits = [0 for x in range(n + 1)]

        # 0 has no set bit
        setBits[0] = 0

        # 1 has a single set bit
        setBits[1] = 1

        # For the rest of the elements
        for i in range(2, n + 1):

            # If current element i is even then
            # it has set bits equal to the count
            # of the set bits in i / 2
            if i % 2 == 0:
                setBits[i] = setBits[i // 2]

                # Else it has set bits equal to one
            # more than the previous element
            else:
                setBits[i] = setBits[i - 1] + 1

        # Sum all the set bits
        for i in range(0, n + 1):
            cnt = cnt + setBits[i]

        return cnt


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_countSetBits(self) -> None:
        sol = Solution()
        for n, solution in ([4, 5], [17, 35]):
            self.assertEqual(solution, sol.countTotalSetBits_solution_1(n))
            self.assertEqual(solution, sol.countTotalSetBits_solution_2(n))
            self.assertEqual(solution, sol.countTotalSetBits_solution_3(n))
            self.assertEqual(solution, sol.countTotalSetBits_solution_4(n))
            self.assertEqual(solution, sol.countTotalSetBits_solution_5(n))


# main
if __name__ == "__main__":
    unittest.main()
