* This is graph traversal problem, so here we have a choice: to use dfs or to use bfs. 

* What is asked: 
    * minimum number of minutes passed until there is no fresh orange. 
    * In graphs it means to find the greatest distance from rotten oranges to any other orange. 
      Usually, if we need to find the distances, we use bfs. 

* So, let me define my variables:
    1. ```m``` and ```n``` are dimensions of our grid, also we have queue to run our bfs and also 
       we want to count number of fresh oranges: we need this to check in the end if all oranges become rotten or not.
    2. We put all rotten oranges coordinates to our queue, so we are going to start from all of them. Also we count number of fresh oranges.
    3. Define directions we can go: four of them and put ```levels = 0```.

* Now, we traverse our grid, using bfs, using level by level traversal: it means, that each time, 
when we have some elements in queue, we popleft all of them and put new neighbours to the end. 
In this way each time we reach line ```levels += 1```, we have nodes with distance which is 1 bigger than previous level. 
In the end ```levels - 1``` will be our answer, because one time in the end 
when we do not have anything to add, levels still be incremented by one.

* Finally, we check if we still have fresh oranges, and if yes, ```return-1```. 
If not, we need to return ```max(levels-1, 0)```, because it can happen, 
that our queue was empty in the beginning and we do not need to subtract 1.

* Complexity: time complexity is ```O(mn)```, because we first traverse our grid to fill queue 
and found number of fresh oranges. Then we use classical bfs, so each node will be added and removed 
from queue at most 1 time. 
Space complexity is also can be ```O(mn)```, we can have for example ```O(mn)``` rotten oranges in the very beginning.