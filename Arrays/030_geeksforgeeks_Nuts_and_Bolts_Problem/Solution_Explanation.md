## Geeks For Geeks : Nuts & Bolts Problem (Lock & Key problem)

Given a set of n nuts of different sizes and n bolts of different sizes. 
There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently. 

**Constraint:** Comparison of a nut to another nut or a bolt to another bolt 
is not allowed. It means nut can only be compared with bolt and bolt can only 
be compared with a nut to see which one is bigger/smaller.

### **Examples:** 

```
Input : nuts[] = {'@', '#', '$', '%', '^', '&'}
        bolts[] = {'$', '%', '&', '^', '@', '#'}
Output : Matched nuts and bolts are-
        $ % & ^ @ # 
        $ % & ^ @ #  
```

Another way of asking this problem is, given a box with locks and keys 
where one lock can be opened by one key in the box. We need to match the pair.

### Solution

1. Traverse the nuts array and create a hashmap
1. Traverse the bolts array and search for it in hashmap.
1. If it is found in the hashmap of nuts then this means bolts exist for that nut. 

```python
from typing import List
from collections import Counter

class Solution(object):

    def matchPairs(self, nuts: List[str],
                   bolts: List[str], n: int) -> List[str]:
        if not nuts or not bolts:
            return []
        if len(nuts) != len(bolts):
            return []

        allowed = ['!','#','$','%','&','*','@','^','~']

        ans = []
        nuts_counter = Counter(nuts)
        bolts_counter = Counter(bolts)
        for i in allowed:
            if ( i in nuts_counter ) and ( i in bolts_counter ):
                ans.append(i)
        print("matched nuts and bolts are-")
        print(*ans)
        print(*ans)
        return ans
```
**Output:**
```
for input:
nuts = ['@', '%', '$', '#', '^']
bolts = ['%', '@', '#', '$', '^']

nuts = ['^', '&', '%', '@', '#', '*', '$', '~', '!']
bolts = ['~', '#', '@', '%', '&', '*', '$', '^', '!']

and output can only contain and has to be in the order:
['!','#','$','%','&','*','@','^','~']

matched nuts and bolts are-
# $ % @ ^
! # $ % & * @ ^ ~
```

**Time Complexity:**
The time complexity for this solution is **O(n)**.
