#
# Time : O(NlogN); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Given arrival and departure times of all trains that reach a railway station.
# Your task is to find the minimum number of platforms required for the railway station so that no train waits.
#
# Note: Consider that all the trains arrive on the same day and leave on the same day. Also, arrival
# and departure times will not be same for a train, but we can have arrival time of one train equal to
# departure of the other. In such cases, we need different platforms, i.e at any given instance of time,
# same platform can not be used for both departure of a train and arrival of another.
#
# Example:
#
# Trains arrival    = { 2.00, 2.10, 3.00, 3.20, 3.50, 5.00 }
# Trains departure  = { 2.30, 3.40, 3.20, 4.30, 4.00, 5.20 }
#
# Minimum platforms needed is 2
#
# Train arrived at 2:00 on platform 1       <=
# Train arrived at 2:10 on platform 2       <=
# Train departed at 2:30 from platform 1    =>
# Train arrived at 3:00 on platform 1       <=
# Train departed at 3:20 from platform 1    =>
# Train arrived at 3:20 on platform 1       <=
# Train departed at 3:40 from platform 2    =>
# Train arrived at 3:50 on platform 2       <=
# Train departed at 4:00 from platform 2    =>
# Train departed at 4:30 from platform 1    =>
# Train arrived at 5:00 on platform 1       <=
# Train departed at 5:20 from platform 1    =>
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/minimum-platforms/0 (GeeksForGeeks - Minimum Platforms)
# Solution Hint: https://www.techiedelight.com/minimum-number-of-platforms-needed-avoid-delay-arrival-train/
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# The idea is to merge arrival and departure time of trains and consider them in sorted order. (Instead of actual
# merging of arrival and departure trains and then sorting them, we can sort arrival and departure of trains and
# follow logic similar to merging of two sorted arrays).
#
# We maintain a counter to count number of trains present at the station at any point of time. The counter also represents
# number of platforms needed at that time.
#
#   + If train is scheduled to arrive next, we increase the counter by 1 and update minimum platforms needed if count
#     is more than minimum platforms needed so far.
#
#   + If train is scheduled to depart next, we decrease the counter by 1.
#
# One special case we need to handle. When two trains are scheduled to arrive and depart at the same time, we depart
# the train first.
#
from typing import List

from bisect import bisect, insort_left

import unittest


class Solution:

    # Function to find minimum number of platforms needed in the
    # station so to avoid any delay in arrival of any train.
    def minPlatforms(self, arrivals: List[int], departures: List[int]) -> int:
        # sort arrival time of trains
        arrivals.sort()

        # sort departure time of trains
        departures.sort()

        # maintains the count of trains
        count = 0

        # stores minimum platforms needed
        platforms = 0

        # take two indices for arrival and departure time
        i = j = 0

        # run till train is scheduled to arrive
        while i < len(arrivals):

            # if train is scheduled to arrive next
            if arrivals[i] < departures[j]:

                # increase the count of trains and update minimum
                # platforms if required
                count = count + 1
                platforms = max(platforms, count)

                # move the pointer to next arrival
                i = i + 1

            # if train is scheduled to depart next i.e.
            # (departure[j] < arrival[i]), decrease the count of trains
            # and move pointer j to next departure

            # If two trains are arriving and departing at the same time, i.e.
            # (arrival[i] == departure[j]) depart the train first
            else:
                count = count - 1
                j = j + 1

        return platforms


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minPlatforms(self) -> None:
        s = Solution()
        for arrivals, departures, solution in (
            [[200, 210, 300, 320, 350, 500], [230, 340, 320, 430, 400, 520], 2],
            [[900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000], 3],
            [[900, 1100, 1235], [1000, 1200, 1240], 1],
        ):
            self.assertEqual(
                solution,
                s.minPlatforms(arrivals, departures),
                "Should return the minimum number of platforms required for the railway station so that no train waits",
            )


if __name__ == "__main__":
    unittest.main()
