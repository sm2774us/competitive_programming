## Google | Phone | Box Stacking Problem

Given a collection of boxes. Return the max number of boxes that you can russian doll.
Each box has (w, h, l).

Example:

Input:

```
[
	[3,9,9],
	[1,4,10],
	[5,10,11],
	[3,9,3],
	[1,5,3]
	[7, 12, 1]
]
```

Output:

```
3
```

Explanation: [1,5,3] fits in [3,9,9] which fits in [5,10,11]
All the dimensions must be smaller to fit into a larger box -- [1,5,3] does not fit into [3,9,3]

This seems to be a variation of the known [Box Stacking Problem](https://practice.geeksforgeeks.org/problems/box-stacking/1).
May be similar to [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) 
question but harder with the extra dimension.

**Source:** [https://leetcode.com/discuss/interview-question/540814/google-phone-box-stacking-problem](https://leetcode.com/discuss/interview-question/540814/google-phone-box-stacking-problem)

**References/Similar Problems:**
* [http://people.csail.mit.edu/bdean/6.046/dp/](http://people.csail.mit.edu/bdean/6.046/dp/) - The link also has video for explanation of solution.
* [GeeksForGeeks - Box Stacking Problem](https://practice.geeksforgeeks.org/problems/box-stacking/1)
* [LeetCode - Problem 354 - Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)