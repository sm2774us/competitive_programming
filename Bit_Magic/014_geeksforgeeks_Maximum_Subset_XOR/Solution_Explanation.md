## Geeks For Geeks : Rightmost different bit

#### **Find the maximum subset XOR of a given set**

Given an set of positive integers. find the maximum XOR subset value in the given set. 

Expected time complexity O(n).

#### **Examples:**

```
Input: set[] = {2, 4, 5}
Output: 7
The subset {2, 5} has maximum XOR value

Input: set[] = {9, 8, 5}
Output: 13
The subset {8, 5} has maximum XOR value

Input: set[] = {8, 1, 2, 12, 7, 6}
Output: 15
The subset {1, 2, 12} has maximum XOR value

Input: set[] = {4, 6}
Output: 6
The subset {6} has maximum XOR value
```

**Note:** that this problem is different from the [maximum subarray XOR](https://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/). 

Here we need to find subset instead of subarray.

#### **Solution:**

A **Simple Solution** is to generate all possible subsets of given set, 
find XOR of every subset and return the subset with maximum XOR.

Below is an **Efficient Algorithm** that works in **O(n)** time.
The idea is based on below facts:

1. Number of bits to represent all elements is fixed which is 32 bits for integer in most of the compilers.
1. If maximum element has Most Significant Bit MSB at position i, then result is at least 2<sup>i</sup>

```
1. Initialize index of chosen elements as 0. Let this index be 
   'index'
2. Traverse through all bits starting from most significant bit. 
   Let i be the current bit.
......(a) Find the maximum element with i'th bit set.  If there
          is no element with i'th bit set, continue to smaller 
          bit.  
......(b) Let the element with i'th bit set be maxEle and index
          of this element be maxInd. Place maxEle at 'index' and
          (by swapping set[index] and set[maxInd]) 
......(c) Do XOR of maxEle with all numbers having i'th  bit as set.
......(d) Increment index 
3. Return XOR of all elements in set[]. Note that set[] is modified
   in step 2.c.
```

Below is the implementation of this algorithm.

```python
```
**Output:**
```
Max subset XOR is 13
```
**Illustration:**
```
Let the input set be : {9, 8, 5}

We start from 31st bit [Assuming Integers are 32 bit 
long]. The loop will continue without doing anything till 4'th bit.

The 4th bit is set in set[0] i.e. 9 and this is the maximum
element with 4th bit set. So we choose this element and check
if any other number has the same bit set. If yes, we XOR that 
number with 9. The element set[1], i.e., 8 also has 4'th bit 
set. Now set[] becomes {9, 1, 5}.  We add 9 to the list of 
chosen elements by incrementing 'index'

We move further and find the maximum number with 3rd bit set
which is set[2] i.e. 5  No other number in the array has 3rd
bit set. 5 is also added to the list of chosen element.

We then iterate for bit 2 (no number for this) and then for 
1 which is 1. But numbers 9 and 5 have the 1st bit set. Thus
we XOR 9 and 5 with 1 and our set becomes (8, 1, 4)

Finally, we XOR current elements of set and get the result
as 8 ^ 1 ^ 4 = 13.
```

#### **How does this work?**

Let us first understand a simple case when all elements have Most Significant Bits (MSBs) at different positions. The task in this particular case is simple, we need to do XOR of all elements.
If input contains multiple numbers with the same MSB, then it’s not obvious which of them we should choose to include in the XOR. What we do is reduce the input list into an equivalent form that doesn’t contain more than one number of the same length. By taking the maximum element, we know that the MSB of this is going to be there in output. Let this MSB be at position i. If there are more elements with i’th set (or same MSB), we XOR them with the maximum number so that the i’th bit becomes 0 in them and problem reduces to i-1 bits.

##### **References:**

[http://math.stackexchange.com/questions/48682/maximization-with-xor-operator](http://math.stackexchange.com/questions/48682/maximization-with-xor-operator)

**Note:** The above method is similar to Gaussian elimination. Consider a matrix of size 32 x n where 32 is number of bits and n is number of elements in array.
