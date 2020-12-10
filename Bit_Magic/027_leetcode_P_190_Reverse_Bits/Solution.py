#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 190: Reverse Bits
#
# Description:
#
# Reverse bits of a given 32 bits unsigned integer.
#
#
# Note:
#
#   * Note that in some languages such as Java, there is no unsigned integer type.
#     In this case, both input and output will be given as a signed integer type.
#     They should not affect your implementation, as the integer's internal binary
#     representation is the same, whether it is signed or unsigned.
#   * In Java, the compiler represents the signed integers using 2's complement notation. Therefore,
#     in Example 2 below, the input represents the signed integer -3 and the output
#     represents the signed integer -1073741825.
#
# Follow up:
#
# If this function is called many times, how would you optimize it?
#
# Example 1:
#
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
#              so return 964176192 which its binary representation is 00111001011110000010100101000000.
#
# Example 2:
#
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
#              so return 3221225471 which its binary representation is 10111111111111111111111111111111.
#
#
# Constraints:
#   * The input must be a binary string of length 32
#
# **************************************************************************
# Source:   https://leetcode.com/problems/reverse-bits/ (LeetCode - Problem 190 - Reverse Bits)
# **************************************************************************
#
#
import unittest


class Solution(object):

    # Solution 1:
    #
    # We are asked to reverse bits in our number. What is the most logical way to do it?
    # Create number ans, process original number bit by bit from end
    # and add this bit to the end of our ans number, and that is all!
    #
    # Why it is works?
    #
    # ans = (ans << 1)^(n & 1) adds last bit of n to ans
    # n >>= 1 removes last bit from n.
    #
    # Imagine number n = 11011010, and ans = 0
    #
    # ans = 0, n = 1101101
    # ans = 01, n = 110110
    # ans = 010, n = 11011
    # ans = 0101, n = 1101
    # ans = 01011, n = 110
    # ans = 010110, n = 11
    # ans = 0101101, n = 1
    # ans = 01011011, n = 0
    #
    # Complexity: time complexity is O(32),
    #             space complexity is O(1).
    #
    # Follow up There is O(5) smart solution which is quite impressive, see the solution below ( Solution 2 ).
    # We also can hash some 8-bits parts, so we can inverse 4 parts on the fly, with time complexity O(4)
    # and memory complexity O(256) (and pre-processing O(256) as well).
    #
    def reverseBits_using_bitwise_operators(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            ans = (ans << 1) ^ (n & 1)
            # Note the bitwise or AKA "|" above can be replaced by the plus operator as shown below:
            # ans = (ans << 1) + (n & 1)
            # This turns out to be more readable and fast in python
            n >>= 1
        return ans

    def rshift(self, val: int, n: int) -> int:
        # return val >> n if val >= 0 else (val + 0x100000000) >> n
        return (val % 0x100000000) >> n

    # Solution 2:
    #
    # for 8 bit binary number abcdefgh, the process is as follows:
    #
    # abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
    #
    # Complexity: time complexity is O(log(num_bits)) since num_bits = 32 => O(log2(32)) = O(5)
    #
    # For a detailed explanation of Solutions 1 [ O(32) ] and 2 [ O(5) ] watch the youtube video:
    # https://youtu.be/-5z9dimxxmI
    #
    # Here's a walkthrough for 964176192 (0000 0010 1001 0100 0001 1110 1001 1100) for a better understanding
    # of what's happening at each step :
    #
    # 	n = (n >> 16) | (n << 16);
    # 	bin(n);	// 0001    1110    1001    1100    0000    0010    1001    0100
    # 	n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
    # 	bin(n);	// 1001    1100    0001    1110    1001    0100    0000    0010
    # 	n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
    # 	bin(n);	// 1100    1001    1110    0001    0100    1001    0010    0000
    # 	n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
    # 	bin(n);	// 0011    0110    1011    0100    0001    0110    1000    0000
    # 	n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
    # 	bin(n);	// 0011    1001    0111    1000    0010    1001    0100    0000
    #
    # Another example:
    #
    # Step 0.
    # abcd efgh ijkl mnop qrst uvwx yzAB CDEF <-- n
    #
    # Step 1.
    #                     abcd efgh ijkl mnop <-- n >> 16, same as (n & 0xffff0000) >> 16
    # qrst uvwx yzAB CDEF                     <-- n << 16, same as (n & 0x0000ffff) << 16
    # qrst uvwx yzAB CDEF abcd efgh ijkl mnop <-- after OR
    #
    # Step 2.
    #           qrst uvwx           abcd efgh <-- (n & 0xff00ff00) >> 8
    # yzAB CDEF           ijkl mnop           <-- (n & 0x00ff00ff) << 8
    # yzAB CDEF qrst uvwx ijkl mnop abcd efgh <-- after OR
    #
    # Step 3.
    #      yzAB      qrst      ijkl      abcd <-- (n & 0xf0f0f0f0) >> 4
    # CDEF      uvwx      mnop      efgh      <-- (n & 0x0f0f0f0f) << 4
    # CDEF yzAB uvwx qrst mnop ijkl efgh abcd <-- after OR
    #
    # Step 4.
    #   CD   yz   uv   qr   mn   ij   ef   ab <-- (n & 0xcccccccc) >> 2
    # EF   AB   wx   st   op   kl   gh   cd   <-- (n & 0x33333333) << 2
    # EFCD AByz wxuv stqr opmn klij ghef cdab <-- after OR
    #
    # Step 5.
    #  E C  A y  w u  s q  o m  k i  g e  c a <-- (n & 0xaaaaaaaa) >> 1
    # F D  B z  x v  t r  p n  l j  h f  d b  <-- (n & 0x55555555) << 1
    # FEDC BAzy xwvu tsrq ponm lkji hgfe dcba <-- after OR
    #
    def reverseBits_using_bitwise_operators_optimized(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        # n = ((n & 0xffff0000) >>> 16) | ((n & 0x0000ffff) << 16)
        n = (self.rshift((n & 0xFFFF0000), 16)) | ((n & 0x0000FFFF) << 16)
        # n = ((n & 0xff00ff00) >>> 8) | ((n & 0x00ff00ff) << 8)
        n = (self.rshift((n & 0xFF00FF00), 8)) | ((n & 0x00FF00FF) << 8)
        # n = ((n & 0xf0f0f0f0) >>> 4) | ((n & 0x0f0f0f0f) << 4)
        n = (self.rshift((n & 0xF0F0F0F0), 4)) | ((n & 0x0F0F0F0F) << 4)
        # n = ((n & 0xcccccccc) >>> 2) | ((n & 0x33333333) << 2)
        n = (self.rshift((n & 0xCCCCCCCC), 2)) | ((n & 0x33333333) << 2)
        # n = ((n & 0xaaaaaaaa) >>> 1) | ((n & 0x55555555) << 1)
        n = (self.rshift((n & 0xAAAAAAAA), 1)) | ((n & 0x55555555) << 1)
        return n

    def reverseBits_oneliner(self, n: int, count: int = 0) -> int:
        """
        :type n: int
        :rtype: int
        """
        return int(bin(n)[2:].zfill(32)[::-1], 2)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reverseBits(self) -> None:
        sol = Solution()
        for n, solution in (
            [0b00000010100101000001111010011100, 964176192],
            [0b11111111111111111111111111111101, 3221225471],
        ):
            self.assertEqual(solution, sol.reverseBits_using_bitwise_operators(n))
            self.assertEqual(
                solution, sol.reverseBits_using_bitwise_operators_optimized(n)
            )
            self.assertEqual(solution, sol.reverseBits_oneliner(n))


# main
if __name__ == "__main__":
    unittest.main()
