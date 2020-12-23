#
# Time :
# Space:
#
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks For Geeks: String Ignorance
#
# Description:
#
# Given a string of both uppercase and lowercase alphabets, the task is to print the string with alternate occurrences of any character dropped(including space and consider upper and lowercase as same).
#
# Input:
# First line consists of T test cases. First line of every test case consists of String S.
#
# Output:
# Single line output, print the updated string.
#
# Constraints:
# 1<=T<=100
# 1<=|String|<=10000
#
# Example:
# Input:
# 2
# It is a long day dear.
# Geeks for geeks
# Output:
# It sa longdy ear.
# Geks fore
#
# Explanation:
# For the 1st test case.
# Print first "I" and then ignore next "i". Similarly print first space then ignore next space. and so on.
#
# **************************************************************************
# Source    : https://practice.geeksforgeeks.org/problems/string-ignorance/0 (GeeksForGeeks - String Ignorance)
#
import unittest


class Solution:

    # Python3 program to print the string
    # in given pattern
    #
    # Function to print the string
    #
    # As we have to print characters in alternate manner,
    # so start traversing the string and perform following two steps :
    #
    #   * Increment the count of occurrence of current character in a hash table.
    #   * Check if the count becomes odd, then print the current character, else not.
    #
    def printStringAlternate(self, string: str) -> str:

        ans = []
        occ = {}

        # Start traversing the string
        for i in range(0, len(string)):

            # Convert uppercase to lowercase
            temp = string[i].lower()

            # Increment occurrence count
            occ[temp] = occ.get(temp, 0) + 1

            # If count is odd then print the character
            if occ[temp] & 1:
                # print(string[i], end="")
                ans.append(string[i])
        # print()
        return "".join(ans)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_printStringAlternate(self) -> None:
        s = Solution()
        for string, solution in (
            ["It is a long day dear.", "It sa longdy ear."],
            ["Geeks for geeks", "Geks fore"],
        ):
            self.assertEqual(solution, s.printStringAlternate(string))


if __name__ == "__main__":
    unittest.main()
