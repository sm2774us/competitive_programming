## Geeks For Geeks : Rightmost different bit

#### **[Problem Statement](https://practice.geeksforgeeks.org/problems/rotate-bits/0) of Rotate bits of a number problem.**

> Given an integer **N** and an integer **D**, you are required 
> to write a program to **rotate the binary representation** of the integer 
> **N by D** digits to the **left** as well as **right** and print the **results** 
> in **decimal values** after each of the rotation.
> 
> **Note:** Integer **N** is stored using **16 bits**, i.e., 
> 12 will be stored as 0000.....001100.
>
> **Input:**
>
> First line of input contains a single integer **T** which denotes 
> the number of test cases. Each test case contains two space 
> separated integers **N** and **D** where **N** denotes the number 
> to be rotated and **D** denotes the number of digits by which 
> the number is required to be rotated.
>
> **Output:**
> 
> For each testcase, in a new line, print the value of 
> number **N** after rotating it to left by **D** digits in **one line**, 
> and **second line** prints the value of number N after rotating 
> it to the **right** by D digits.
>
> **Constraints:**
> * 1 <= T <= 100
> * 1 <= N <  216
> * 1 <= D <= 105
>
> **Example:**
> 
> ___Input:___
> 
> 2
> 
> 229 3
> 
> 28 2
>
> ___Output:___
> 
> 1832
> 
> 40988
> 
> 112
> 
> 7
>

#### Solution

```python
#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Rotate Bits
#
# Description:
#
# Given an integer N and an integer D, you are required to write a program to rotate the binary representation of the integer N by D digits to the left as well as right and print the results in decimal values after each of the rotation.
# Note: Integer N is stored using 16 bits. i.e. 12 will be stored as 0000.....001100.
#
# Input:
# First line of input contains a single integer T which denotes the number of test cases. Each test case contains two space separated integers N and D where N denotes the number to be rotated and D denotes the number of digits by which the number is required to be rotated.
#
# Output:
# For each testcase, in a new line, print the value of number N after rotating it to left by D digits in one line, and second line prints the value of number N after rotating it to the right by D digits.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <  216
# 1 <= D <= 105
#
# Example:
# Input:
# 2
# 229 3
# 28 2
# Output:
# 1832
# 40988
# 112
# 7
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/rotate-bits/0 (GeeksForGeeks - Rotate Bits)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import unittest

INT_BITS = 32

class Solution(object):

    # Bit Rotation: A rotation (or circular shift) is an operation similar to shift
    # except that the bits that fall off at one end are put back to the other end.
    #
    # Left Rotation> In left rotation, the bits that fall off at left end are put back at right end.
    #
    # Right Rotation> In right rotation, the bits that fall off at right end are put back at left end.

    # Function to left
    # rotate n by d bits
    def leftRotate(self, n, d):
        # In n<<d, last d bits are 0.
        # To put first 3 bits of n at
        # last, do bitwise or of n<<d
        # with n >>(INT_BITS - d)
        return (n << d) | (n >> (INT_BITS - d))

    # Function to right
    # rotate n by d bits
    def rightRotate(self, n, d):
        # In n>>d, first d bits are 0.
        # To put last 3 bits of at
        # first, do bitwise or of n>>d
        # with n <<(INT_BITS - d)
        return (n >> d) | (n << (INT_BITS - d)) & 0xFFFFFFFF

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_leftRotate(self) -> None:
        sol = Solution()
        for n, d, solution in (
                [16, 2, 64],
                [229, 3, 1832],
                [28, 2, 112]
        ):
            self.assertEqual(solution, sol.leftRotate(n, d))



    def test_rightRotate(self) -> None:
        sol = Solution()
        for n, d, solution in (
                [16, 2, 4],
                [229, 3, 2684354588],       # GeeksForGeeks webpage (https://practice.geeksforgeeks.org/problems/rotate-bits/0) has the output value as 40988 should be 2684354588 instead.
                [28, 2, 7]
        ):
            self.assertEqual(solution, sol.rightRotate(n, d))

# main
if __name__ == "__main__":
    unittest.main()
```