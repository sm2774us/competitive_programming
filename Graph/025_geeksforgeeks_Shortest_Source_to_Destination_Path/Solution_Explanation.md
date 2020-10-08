## GeeksForGeeks - Shortest path in a Binary Maze

Given a MxN matrix where each element can either be 0 or 1. We need to find the shortest path between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1.

Expected time complexity is O(MN).

For example –

```
Input:
mat[ROW][COL]  = {{1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
                  {1, 0, 1, 0, 1, 1, 1, 0, 1, 1 },
                  {1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
                  {1, 1, 1, 0, 1, 1, 1, 0, 1, 0 },
                  {1, 0, 1, 1, 1, 1, 0, 1, 0, 0 },
                  {1, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
                  {1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
                  {1, 1, 0, 0, 0, 0, 1, 0, 0, 1 }};
Source = {0, 0};
Destination = {3, 4};

Output:
Shortest Path is 11 
```

The idea is inspired from [Lee algorithm](https://en.wikipedia.org/wiki/Lee_algorithm) and uses BFS.

    1. We start from the source cell and calls BFS procedure.
    2. We maintain a queue to store the coordinates of the matrix and initialize it with the source cell.
    3. We also maintain a Boolean array visited of same size as our input matrix and initialize all its elements to false.
        1. We LOOP till queue is not empty
        2. Dequeue front cell from the queue
        3. Return if the destination coordinates have reached.
        4. For each of its four adjacent cells, if the value is 1 and they are not visited yet, we enqueue it in the queue and also mark them as visited.

**Note** that [BFS](http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/) works here because it doesn’t consider a single path at once. It considers all the paths starting from the source and moves ahead one unit in all those paths at the same time which makes sure that the first time when the destination is visited, it is the shortest path.

#### Implementation

Below is the implementation of the idea –

```python
# Python program to find the shortest
# path between a given source cell
# to a destination cell.

from collections import deque

ROW = 9
COL = 10

# To store matrix cell cordinates
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # A data structure for queue used in BFS


class QueueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt  # The cordinates of the cell
        self.dist = dist  # Cell's distance from the source


class Solution:
    # Check whether given cell(row,col)
    # is a valid cell or not
    def isValid(self, row: int, col: int):
        return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

    # Function to find the shortest path between ( uses BFS )
    # a given source cell to a destination cell.
    def shortestPath(self, mat, src: Point, dest: Point):
        # These arrays are used to get row and column
        # numbers of 4 neighbours of a given cell
        rowNum = [-1, 0, 0, 1]
        colNum = [0, -1, 1, 0]

        # check source and destination cell
        # of the matrix have value 1
        if mat[src.x][src.y] != 1 or mat[dest.x][dest.y] != 1:
            return -1

        visited = [[False for i in range(COL)] for j in range(ROW)]

        # Mark the source cell as visited
        visited[src.x][src.y] = True

        # Create a queue for BFS
        q = deque()

        # Distance of source cell is 0
        s = QueueNode(src, 0)
        q.append(s)  # Enqueue source cell

        # Do a BFS starting from source cell
        while q:

            curr = q.popleft()  # Dequeue the front cell

            # If we have reached the destination cell,
            # we are done
            pt = curr.pt
            if pt.x == dest.x and pt.y == dest.y:
                return curr.dist

                # Otherwise enqueue its adjacent cells
            for i in range(4):
                row = pt.x + rowNum[i]
                col = pt.y + colNum[i]

                # if adjacent cell is valid, has path
                # and not visited yet, enqueue it.
                if (
                    self.isValid(row, col)
                    and mat[row][col] == 1
                    and not visited[row][col]
                ):
                    visited[row][col] = True
                    Adjcell = QueueNode(Point(row, col), curr.dist + 1)
                    q.append(Adjcell)

                    # Return -1 if destination cannot be reached
        return -1


# main
if __name__ == "__main__":
    # Driver code
    sol = Solution()
    mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
           [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]
    source = Point(0, 0)
    dest = Point(3, 4)

    dist = sol.shortestPath(mat, source, dest)

    if dist != -1:
        print("Shortest Path is", dist)
    else:
        print("Shortest Path doesn't exist")
```
____

#### Output:

```
Shortest Path is 11
```
