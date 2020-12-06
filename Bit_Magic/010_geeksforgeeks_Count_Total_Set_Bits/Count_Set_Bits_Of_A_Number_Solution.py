#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Count set bits in an integer
# Write an efficient program to count number of 1s in binary representation of an integer.
#
# Examples :
#
# Input : n = 6
# Output : 2
# Binary representation of 6 is 110 and has 2 set bits
#
# Input : n = 13
# Output : 3
# Binary representation of 13 is 1101 and has 3 set bits
#
# **************************************************************************
# Source: https://www.geeksforgeeks.org/count-set-bits-in-an-integer/ (GeeksForGeeks - Count set bits in an integer)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
# https://www.geeksforgeeks.org/count-set-bits-using-python-list-comprehension/
#
import unittest


class Solution(object):
    BitsSetTable256 = [0] * 256
    num_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

    # Function to initialise the lookup table
    def __init__(self):
        # To initially generate the
        # table algorithmically
        self.BitsSetTable256[0] = 0
        for i in range(256):
            self.BitsSetTable256[i] = (i & 1) + self.BitsSetTable256[i // 2]

    # Solution 1: Simple Method
    #
    #             Loop through all bits in an integer,
    #             check if a bit is set and if it is then increment the set bit count.
    #
    # Time Complexity: O(logN)

    # Function to get no of set bits in binary
    # representation of positive integer n
    def countSetBits_solution_1(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    # Solution 2: Recursive Approach
    #

    # Function to get no of set bits in binary
    # representation of positive integer n
    def countSetBits_solution_2(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        else:
            # if last bit set add 1 else
            # add 0
            return (n & 1) + self.countSetBits_solution_2(n >> 1)

    # Solution 3: Brian Kernighan’s Algorithm
    #

    # Subtracting 1 from a decimal number flips all the bits after the rightmost set bit(which is 1) including the rightmost set bit.
    # for example :
    # 10 in binary is 00001010
    # 9 in binary is 00001001
    # 8 in binary is 00001000
    # 7 in binary is 00000111
    # So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the rightmost set bit.
    # If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
    # The beauty of this solution is the number of times it loops is equal to the number of set bits in a given integer.

    #    1  Initialize count: = 0
    #    2  If integer n is not zero
    #       (a) Do bitwise & with (n-1) and assign the value back to n
    #           n: = n&(n-1)
    #       (b) Increment count by 1
    #       (c) go to step 2
    #    3  Else return count

    # Function to get no of set bits in binary
    # representation of positive integer n
    def countSetBits_solution_3(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1

        return count

    # Solution 4: Brian Kernighan’s Algorithm - Recursive Approach
    #

    # Function to get no of set bits in binary
    # representation of positive integer n
    def countSetBits_solution_4(self, n: int) -> int:
        # base case
        if n == 0:
            return 0
        else:
            return 1 + self.countSetBits_solution_4(n & (n - 1))

    # Solution 5: Using Lookup Table
    #

    # Function to return the count
    # of set bits in n
    def countSetBits_solution_5(self, n: int) -> int:
        return (
            self.BitsSetTable256[n & 0xFF]
            + self.BitsSetTable256[(n >> 8) & 0xFF]
            + self.BitsSetTable256[(n >> 16) & 0xFF]
            + self.BitsSetTable256[n >> 24]
        )

    # Solution 6: Mapping numbers with the bit
    #

    # Time Complexity: O(1)
    #
    # Storage Complexity: O(1) Whether given number is short, int, long or long long
    # we require array of 16 size only which is constant.
    #
    #

    # Function to return the count
    # of set bits in n
    def countSetBits_solution_6(self, n: int) -> int:
        nibble = 0
        if 0 == n:
            return self.num_to_bits[0]

            # Find last nibble
        nibble = n & 0xF

        # Use pre-stored values to find count
        # in last nibble plus recursively add
        # remaining nibbles.

        return self.num_to_bits[nibble] + self.countSetBits_solution_6(n >> 4)

    # Solution 7: Using List comprehension
    #

    # We will solve this problem in Python using List comprehension. Approach is simple,
    #
    #   1. Convert given number into it’s binary representation using bin(number) function.
    #   2. Now separate out all 1’s from binary representation of given number and print length of list of 1’s.
    #

    # Function to get no of set bits in binary
    # representation of positive integer n
    def countSetBits_solution_7(self, n: int) -> int:
        # convert given number into binary
        # output will be like bin(11)=0b1101
        binary = bin(n)

        # now separate out all 1's from binary string
        # we need to skip starting two characters
        # of binary string i.e; 0b
        setBits = [ones for ones in binary[2:] if ones == "1"]
        return len(setBits)

    # Solution 5: one-liner
    # return bin(n).count("1")
    #

    # Function to get no of set bits in binary
    # representation of positive integer n
    def countSetBits_solution_8_oneliner(self, n: int) -> int:
        return bin(n).count("1")


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_countSetBits(self) -> None:
        sol = Solution()
        for n, solution in ([4, 1], [17, 2]):
            self.assertEqual(solution, sol.countSetBits_solution_1(n))
            self.assertEqual(solution, sol.countSetBits_solution_2(n))
            self.assertEqual(solution, sol.countSetBits_solution_3(n))
            self.assertEqual(solution, sol.countSetBits_solution_4(n))
            self.assertEqual(solution, sol.countSetBits_solution_5(n))
            self.assertEqual(solution, sol.countSetBits_solution_6(n))
            self.assertEqual(solution, sol.countSetBits_solution_7(n))
            self.assertEqual(solution, sol.countSetBits_solution_8_oneliner(n))


# main
if __name__ == "__main__":
    unittest.main()
