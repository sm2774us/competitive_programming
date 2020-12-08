#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Computing The Parity Of A Word
#
# Description:
#
# The parity of a binary word is 1 if the number of Is in the word is odd; otherwise,
# it is 0. For example, the parity of 1011 is 1, and the parity of 10001000 is 0. Parity
# checks are used to detect single bit errors in data storage and communication. It is
# fairly straightforward to write code that computes the parity of a single 64-bit word.
#
# How would you compute the parity of a very large number of 64-bit words?
#
# Hint: Use a lookup table, but don't use 264 entries!
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/parity.py (EPI - Computing The Parity Of A Word)
# **************************************************************************
#
from typing import List
import unittest

#
# Note that we could have combined caching with word-level operations, e.g., by
# doing a lookup once we get to 16 bits. The actual run-times depend on the input
# data, e.g., the refinement of the brute-force algorithm is very fast on sparse inputs.
# However, for random inputs, the refinement of the brute-force is roughly 20% faster
# than the brute-force algorithm. The table-based approach is four times faster still,
# and using associativity reduces run time by another factor of two.
#
class Solution(object):
    def __init__(self):
        self.PRECOMPUTED_PARITY = [
            self.parity_solution_4_xor_associativity(i) for i in range(1 << 16)
        ]

    # Solution 1 : Brute Force
    #
    # The brute-force algorithm iteratively tests the value of each bit while track¬
    # ing the number of Is seen so far. Since we only care if the number of Is is even or
    # odd, we can store the number modulo 2.
    #
    # Time Complexity: O(n), where n is the word size.
    #
    def parity_solution_1_brute_force(self, x):
        result = 0
        while x:
            result ^= x & 1
            x >>= 1
        return result

    # Solution 2 : Drop the lowest set bit ( Refinement of the Brute-Force algorithm )
    #
    # The expression `x & (x - 1)` clears the LSB - Least Significant Bit ( i.e., the lowest set bit ).
    #
    # This can be used to improve performance in the best- and average-cases.
    #
    # Let k be the number of bits set to 1 in a particular word. (For example, for 10001010, k = 3.)
    # Then time complexity of the algorithm above is O(k).
    #
    # Time Complexity: O(k), where k is the number of bits set to 1 in a particular word
    #
    def parity_solution_2_clear_LSB(self, x):
        result = 0
        while x:
            result ^= 1
            x &= x - 1  # Drops the lowest set bit of x.
        return result

    # Solution 3 : A precomputed lookup table based solution
    #
    # The problem statement refers to computing the parity for a very large number
    # of words. When you have to perform a large number of parity computations, and,
    # more generally, any kind of bit fiddling computations, two keys to performance are
    # processing multiple bits at a time and caching results in an array-based lookup table.
    #
    # First we demonstrate caching. Clearly, we cannot cache the parity of every 64-bit
    # integer—we would need 264 bits of storage, which is of the order of ten trillion exabytes.
    # However, when computing the parity of a collection of bits, it does not matter
    # how we group those bits, i.e., the computation is associative. Therefore, we can compute
    # the parity of a 64-bit integer by grouping its bits into four non-overlapping 16 bit
    # sub-words, computing the parity of each sub-word, and then computing the parity of
    # these four sub-results. We choose 16 since 216 = 65536 is relatively small, which makes
    # it feasible to cache the parity of all 16-bit words using an array. Furthermore, since
    # 16 evenly divides 64, the code is simpler than if we were, for example, to use 10 bit
    # sub-words.
    #
    # We illustrate the approach with a lookup table for 2-bit words. The cache is
    # (0,1,1,0}—these are the parities of (00),(01),(10),(11), respectively. To compute the
    # parity of (11001010) we would compute the parities of (11), (00), (10), (10). By table
    # lookup we see these are 0,0,1,1, respectively,so the final result is the parity of 0,0,1,1
    # which is 0.
    #
    # To lookup the parity of the first two bits in (11101010), we right shift by 6, to get
    # (00000011), and use this as an index into the cache. To lookup the parity of the next
    # twobits, i.e., (10), we rightshift by 4, to get (10) in the two least-significant bit places.
    # The right shift does not remove the leading (11)—it results in (00001110). We cannot
    # index the cache with this, it leads to an out-of-bounds access. To get the last two
    # bits after the right shift by 4, we bitwise-AND (00001110) with (00000011) (thisis the
    # "mask" used to extract the last 2 bits). The result is (00000010). Similar masking is
    # needed for the two other 2-bit lookups.
    #
    # The time complexity is a function of the size of the keys used to index the lookup
    # table. Let L be the width of the words for which we cache the results, and n the
    # word size. Since there are n/L terms, the time complexity is O(n/L),
    # assuming word-level operations, such as shifting, take O(1) time.
    # (This does not include the time for initialization of the lookup table.)
    #
    # Time Complexity: O(n/L)
    #                           L : the width of the words for which we cache the results
    #                           n : the word size
    #
    def parity_solution_3_precomputed_lookup_table(self, x):
        MASK_SIZE = 16
        BIT_MASK = 0xFFFF
        return (
            self.PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)]
            ^ self.PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK]
            ^ self.PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK]
            ^ self.PRECOMPUTED_PARITY[x & BIT_MASK]
        )

    # Solution 4 : Solution using XOR bitwise operation and Associativity
    #
    # The XOR of two bits is 0 if both bits are 0 or both bits are 1; otherwise it is 1.
    # XOR has the property of being associative (as previously described), as well as commutative,
    # i.e., the order in which we perform the XORs does not change the result. The XOR of
    # a group of bits is its parity. We can exploit this fact to use the CPU's word-level XOR
    # instruction to process multiple bits at a time.
    #
    # For example, the parity of <b63,b62,...,b3,b2,b1,bo> equals the parity of the XOR
    # of <b63, b62,..., b32> and <b31, b30,...,b0>. The XOR of these two 32-bit values can be
    # computed with a single shift and a single 32-bit XOR instruction. We repeat the same
    # operation on 32-, 16-, 8-, 4-, 2-, and 1-bit operands to get the final result. Note that the
    # leading bits are not meaningful, and we have to explicitly extract the result from the
    # least-significant bit.
    #
    # We illustrate the approach with an 8-bit word. The parity of (11010111) is the same
    # as the parity of (1101) XORed with (0111), i.e., of (1010). This in turn is the same
    # as the parity of (10) XORed with (10), i.e., of (00). The final result is the XOR of (0)
    # with (0), i.e., 0. Note that the first XOR yields (11011010), and only the last 4 bits are
    # relevant going forward. The second XOR yields (11101100), and only the last 2 bits
    # are relevant. The third XOR yields (10011010). The last bit is the result, and to extract
    # it we have to bitwise-AND with (00000001).
    #
    # Time Complexity: O(log n) , where n is the word size.
    #
    def parity_solution_4_xor_associativity(self, x):
        x ^= x >> 32
        x ^= x >> 16
        x ^= x >> 8
        x ^= x >> 4
        x ^= x >> 2
        x ^= x >> 1
        return x & 0x1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_parity(self) -> None:
        sol = Solution()
        for x, solution in (
            [568184680, 1],
            [56, 1],
            [5443530242318502, 1],
            [29469493683482, 1],
            [55042960196257, 0],
            [31757824034208103, 0],
            [31564787, 1],
            [168618482290043, 0],
            [5794530425053671, 0],
            [161247358015, 1],
            [855, 1],
            [4184, 0],
        ):
            self.assertEqual(solution, sol.parity_solution_1_brute_force(x))
            self.assertEqual(solution, sol.parity_solution_2_clear_LSB(x))
            self.assertEqual(
                solution, sol.parity_solution_3_precomputed_lookup_table(x)
            )
            self.assertEqual(solution, sol.parity_solution_4_xor_associativity(x))


# main
if __name__ == "__main__":
    unittest.main()
