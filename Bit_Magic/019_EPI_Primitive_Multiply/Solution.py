#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Primitive Multiply
#
# Description:
#
# Write a program that multiplies two non-negative integers. The only operators you
# are allowed to use are
# • assignment,
# • the bitwise operators », «, |, &, ^ and
# • equality checks and Boolean combinations thereof.
#
# You may use loops and functions that you write yourself. These constraints imply,
# for example, that you cannot use increment or decrement, or test if x < y.
#
# Hint: Add using bitwise operations; multiply using shift-and-add.
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/primitive_multiply.py (EPI - Primitive Multiply)
# **************************************************************************
#
from typing import List
import unittest


class Solution(object):

    # A brute-force approach would be to perform repeated addition, i.e., initial¬
    # ize the result to 0 and then add x to it y times. For example, to form 5x3, we would
    # start with 0 and repeatedly add 5, i.e., form 0 + 5,5 + 5,10 + 5. The time complexity
    # is very high—as much as O(2^n), where n is the number of bits in the input, and it
    # still leaves open the problem of adding numbers without the presence of an add
    # instruction.

    # Solution: Grade-School Multiplication Algorithm.
    #
    # The algorithm taught in grade-school for decimal multiplication does not use
    # repeated addition—it uses shift and add to achieve a much better time complexity.
    # We can do the same with binary numbers—to multiply `x` and `y` we initialize the result
    # to 0 and iterate through the bits of `x`, adding `2^k * y` to the result if the k'th bit of `x` is 1.
    #
    # The value (2^k * y) can be computed by left-shifting `y` by `k`. Since we cannot use add
    # directly, we must implement it. We apply the grade-school algorithm for addition to
    # the binary case, i.e., compute the sum bit-by-bit, and "rippling" the carry along.
    #
    # As an example, we show how to multiply 13 = (1101)2 and 9 = (1001)2 using the
    # algorithm described above. In the first iteration, since the LSB of 13 is 1, we set the
    # result to (1001)2. The second bit of (1101)2 is 0, so we move on to the third bit. This
    # bit is 1,so we shift (1001)2 to the left by 2 to obtain (100100)2, which we add to (1001)2
    # to get (101101)2. The fourth and final bit of (1101)2 is 1, so we shift (1001)2 to the left
    # by 3 to obtain (1001000)2, which we add to (101101)2 to get (1110101)2 = 117.
    #
    # Each addition is itself performed bit-by-bit. For example, when adding (101101)2
    # and (1001000)2, the LSB of the result is 1 (since exactly one of the two LSBs of the
    # operands is 1). The next bit is 0 (since both the next bits of the operands are 0). The
    # next bit is 1 (since exactly one of the next bits of the operands is 1). The next bit is
    # 0 (since both the next bits of the operands are 1). We also "carry" a 1 to the next
    # position. The next bit is1(since the carry-in is1and both the next bits of the operands
    # are 0). The remaining bits are assigned similarly.
    #
    # Time Complexity: O(n^2)
    #                           n : the width of the operands.
    #
    # The time complexity of addition is O(n),where n is the width of the operands. Since
    # we do n additions to perform a single multiplication, the total time complexity is
    # O(n^2).
    #
    def multiply(self, x, y):
        def add(a, b):
            running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
            while temp_a or temp_b:
                ak, bk = a & k, b & k
                carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
                running_sum |= ak ^ bk ^ carryin
                carryin, k, temp_a, temp_b = (
                    carryout << 1,
                    k << 1,
                    temp_a >> 1,
                    temp_b >> 1,
                )
            return running_sum | carryin

        running_sum = 0
        while x:  # Examines each bit of x.
            if x & 1:
                running_sum = add(running_sum, y)
            x, y = x >> 1, y << 1
        return running_sum

    def multiply_optimized(self, x: int, y: int) -> int:
        def add(a, b):
            return a if b == 0 else add(a ^ b, (a & b) << 1)

        running_sum = 0
        while x:  # Examines each bit of x.
            if x & 1:
                running_sum = add(running_sum, y)
            x, y = x >> 1, y << 1
        return running_sum


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_primitive_multiply(self) -> None:
        sol = Solution()
        for x, y, solution in (
            [0, 0, 0],
            [0, 1, 0],
            [0, 65533, 0],
            [1, 65533, 65533],
            [345, 1, 345],
            [345, 0, 0],
            [57536, 2187, 125831232],
            [4639, 45265, 209984335],
        ):
            self.assertEqual(solution, sol.multiply(x, y))
            self.assertEqual(solution, sol.multiply_optimized(x, y))


# main
if __name__ == "__main__":
    unittest.main()
