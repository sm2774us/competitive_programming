# Leetcode - Problem 319 - Bulb Switcher

## Problem Description:

There are `n` bulbs that are initially off. You first turn on all the bulbs, 
then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
For the ___i<sup>th</sup>___ round, you toggle every `i` bulb. 
For the ___n<sup>th</sup>___ round, you only toggle the last bulb.

Return ___the number of bulbs that are on after `n` rounds___.

### Example 1:

![Example 1](Image_1.jpg)

```
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
```

### Example 2:

```
Input: n = 0
Output: 0
```
### Example 2:

```
Input: n = 0
Output: 0
```

#### Constraints:

* 0 <= n <= 109