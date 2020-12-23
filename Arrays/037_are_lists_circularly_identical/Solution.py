#
# Time :
# Space:
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# For instance, I have lists:
#
# a[0] = [1, 1, 1, 0, 0]
# a[1] = [1, 1, 0, 0, 1]
# a[2] = [0, 1, 1, 1, 0]
# # and so on
# They seem to be different, but if it is supposed that the start and the end are connected,
# then they are circularly identical.
#
# The problem is, each list which I have has a length of 55 and contains only three ones and 52 zeros in it.
# Without circular condition, there are 26,235 (55 choose 3) lists. However, if the condition 'circular' exists,
# there are a huge number of circularly identical lists
#
# Currently I check circularly identity by following:
#
# def is_dup(a, b):
#     for i in range(len(a)):
#         if a == list(numpy.roll(b, i)): # shift b circularly by i
#             return True
#     return False
# This function requires 55 cyclic shift operations at the worst case.
# And there are 26,235 lists to be compared with each other.
# In short, I need 55 * 26,235 * (26,235 - 1) / 2 = 18,926,847,225 computations.
# It's about nearly 20 Giga!
#
# Is there any good way to do it with less computations? Or any data types that supports circular?
#
# **************************************************************************
# Source:
#   https://stackoverflow.com/questions/26924836/how-to-check-whether-two-lists-are-circularly-identical-in-python (StackOverflow - How to check whether two lists are circularly identical in Python)
# **************************************************************************
#
from typing import List
import re

import unittest


class Solution:

    # Solution 1 -
    #
    # First off, this can be done in O(n) in terms of the length of the list.
    # You can notice that if you will duplicate your list 2 times ([1, 2, 3]) will be [1, 2, 3, 1, 2, 3]
    # then your new list will definitely hold all possible cyclic lists.
    #
    # So all you need is to check whether the list you are searching is inside a 2 times of your starting list.
    # In python you can achieve this in the following way (assuming that the lengths are the same).
    #
    # list1 = [1, 1, 1, 0, 0]
    # list2 = [1, 1, 0, 0, 1]
    # print ' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2))
    #
    # Some explanation about my oneliner: list * 2 will combine a list with itself, map(str, [1, 2])
    # convert all numbers to string and ' '.join() will convert array ['1', '2', '111'] into a string '1 2 111'.
    #
    # As pointed by some people in the comments, oneliner can potentially give some false positives,
    # so to cover all the possible edge cases, the solution presented below:
    #
    # P.S.1 when speaking about time complexity, it is worth noticing that O(n) will be achieved
    # if substring can be found in O(n) time. It is not always so and depends
    # on the implementation in your language (although potentially it can be done in linear time KMP for example).
    #
    # P.S.2 for people who are afraid strings operation and due to this fact think that the answer is not good.
    # What is important is complexity and speed.
    # This algorithm potentially runs in O(n) time and O(n) space which makes it much
    # better than anything in O(n^2) domain.
    # To see this by yourself, you can run a small benchmark
    # (creates a random list pops the first element and appends it to the end thus creating a cyclic list.
    #  You are free to do your own manipulations)
    #
    # Example:
    # ------------------------------------
    # from random import random
    # bigList = [int(1000 * random()) for i in xrange(10**6)]
    # bigList2 = bigList[:]
    # bigList2.append(bigList2.pop(0))
    #
    # # then test how much time will it take to come up with an answer
    # from datetime import datetime
    # startTime = datetime.now()
    # print isCircular(bigList, bigList2)
    # print datetime.now() - startTime    # please fill free to use timeit, but it will give similar results
    # ------------------------------------
    # TC: O(N)
    # SC: O(N)
    #
    # Reference: https://stackoverflow.com/a/26924896
    def is_circular_solution_1(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False

        str1 = " ".join(map(str, arr1))
        str2 = " ".join(map(str, arr2))
        if len(str1) != len(str2):
            return False

        return str1 in str2 + " " + str2

    def is_circular_solution_1a(self, lst1, lst2):
        if len(lst1) != len(lst2):
            return False
        lst1, lst2 = map(str, lst1), map(str, lst2)
        len_longest_element = max(map(len, lst1))
        template = "{{:{}}}".format(len_longest_element)
        circ_lst = " ".join([template.format(el) for el in lst1]) * 2
        return " ".join([template.format(el) for el in lst2]) in circ_lst

    def is_circular_solution_2(self, lst1, lst2):
        if len(lst2) != len(lst2):
            return False
        return bool(
            re.search(
                r"\b{}\b".format(" ".join(map(str, lst2))), " ".join(map(str, lst1)) * 2
            )
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isCircular(self) -> None:
        s = Solution()
        for lst1, lst2, solution in (
            [[0, 9, -1, 2, -1], [-1, 2, -1, 0, 9], True],
            [[2, 9, -1, 0, -1], [-1, 2, -1, 0, 9], False],
            [["Hello" "Circular", "World"], ["World", "Hello" "Circular"], True],
            [["Hello" "Circular", "World"], ["Circular", "Hello" "World"], False],
        ):
            self.assertEqual(solution, s.is_circular_solution_1(lst1, lst2))
            # self.assertEqual(
            #     solution,
            #     s.is_circular_solution_1a(lst1, lst2)
            # )
            # self.assertEqual(
            #     solution,
            #     s.is_circular_solution_2(lst1, lst2)
            # )


if __name__ == "__main__":
    unittest.main()
