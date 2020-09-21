Space and Runtime analysis:
-------------------------------

```s.count(l)``` takes ```O(n)``` and is called ```|Σ|``` times, where ```|Σ|``` is the size of the alphabet. 
This takes ```O( |Σ| * n)```. 
Since the alphabet in this question is just lowercase letters, 
```|Σ| = 26``` so this is ```O(26 * n) ∈ O(n)```.

```s.index(l)``` also takes ```O(n)``` and is called ```|Σ|``` times. 
This takes ```O( |Σ| * n)```, or ```O(n)``` since ```|Σ|``` is constant.

min(index) takes ```O(|Σ|) -> O(1)``` time.

For space, ```index=[s.index(l) for l in letters if s.count(l) == 1]``` takes ```O(|Σ|)``` space.

The overall runtime is ```O( |Σ| * n)```, or ```O(n)``` because the size of the alphabet is constant.