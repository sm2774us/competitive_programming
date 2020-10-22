## LeetCode - Problem 646 - Maximum Length of Pair Chain

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

##### Example 1:

```
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
```

### Solution
It is easy to think about sorting the list firstly. However, it is not so easy to find such an elegant solution. Meanwhile when should we sort from end when should we sort from the start, it is a critical thing we have to figure out. Fortunately, we only have 3 cases for both sorting by start or sorting by end and they are summarized as bellow:

**1. sort by end:** after sorting we know: s1<e1<e2 and s2<e2
(in order to make it be easier, we do not consider about "==" case).
s2 has three possible positions : (first) s1 (second) e1 (third) e2
Hence, we have 3 cases.

___case 1: s2 < s1 < e1 < e2___
```
                         #s1****e1
         #s2*****************************e2
```
___case 2: s1 < s2 < e1 < e2___
```
         #s1*****************e1
                      #s2*******************e2
```
___case 3: s1 < e1 < s2 < e2___
```
        #s1************e1
                                     #s2**************e2
```

**2. sort by start:** we have three cases to put e1 into different locations.

___case1: s1 < e1 < s2 < e2___
```
         #s1******e1
                                     #s2************e2
```
___case2: s1 < s2 < e1 < e2___
```
         #s1***************e1
                     #s2**********************e2
```
___case3: s1 < s2 < e2 < e1___
```
          #s1************************************e1
                          #s2********e2
```
From the summary, we can see: for the 3cases of sorting by start and sorting by end only one case is different, the rest two cases are the same. The different one is case1 of sorting by end and case 3 of sorting by start. By knowing this, it might be helpful to figure out whether we should sort by start or sort by end. After we figure all those out, it is easier to understand the solution.

```python
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        startTimes = [i[0] for i in intervals]
        endTimes = [i[1] for i in intervals]
        startTimes = sorted(startTimes)
        endTimes = sorted(endTimes)
        rooms = 0
        while(len(startTimes) > 0):
            startTime = startTimes.pop(0)
            #now a meeting is going to start, is there a meeting ends
            #(meaning a meeting room is released)?
            endTime = endTimes[0]
            if endTime <= startTime:
                endTimes.pop(0)
            else:
                #need to ask for a new room
                rooms += 1
        return rooms
```

### Python 3 knowledge points

There are a couple of Python 3 knowledge points I can learn from above:

1] How to form a list from an existing tuple list but only take, for example, the second part of each tuple.
> ___`endTimes = [i[1] for i in intervals]`___
>

2] Use list pop with index. Please note that if you write
> ___`x = [1,2,3].pop()`___
>
x will be 3. So if you intend to get the first item, you need to
> ___`x = [1,2,3].pop(0)`___
>
The beauty of this is, after pop(), the list will become [2,3], so next time you can still use pop(0) to retrieve the second of the original list without moving a pointer.

3] The function sorted()

It’s pretty handy, isn’t it? Remember, if you want to calculate is time complexity, you can say it’s O(N logN) since it’s the best average sorting time complexity.
Also, if you want to sort a list reversely, you can set reverse=True like:
> ___`sorted([2,1,4,3]) #will return [1,2,3,4]`___
>
> ___`sorted([2,1,4,3], reverse=True) #will return [4,3,2,1]`___
>