# Breadth first search



Traversal means visiting all the nodes of a graph. Breadth first traversal or Breadth first Search is a recursive algorithm for searching all the vertices of a graph or tree data structure. In this article, you will learn with the help of examples the BFS algorithm, BFS pseudocode and the code of the breadth first search algorithm with implementation in C++, C, Java and Python programs.

## BFS algorithm

A standard DFS implementation puts each vertex of the graph into one of two categories:

1. Visited
2. Not Visited

The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

The algorithm works as follows:

1. Start by putting any one of the graph's vertices at the back of a queue.
2. Take the front item of the queue and add it to the visited list.
3. Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
4. Keep repeating steps 2 and 3 until the queue is empty.

The graph might have two different disconnected parts so to make sure that we cover every vertex, we can also run the BFS algorithm on every node

## BFS example

Let's see how the Breadth First Search algorithm works with an example. We use an undirected graph with 5 vertices.

![undirected graph with 5 vertices](https://cdn.programiz.com/sites/tutorial2program/files/graph-bfs-step-0.jpg)

We start from vertex 0, the BFS algorithm starts by putting it in the Visited list and putting all its adjacent vertices in the stack.

![visit start vertex and add its adjacent vertices to queue](https://cdn.programiz.com/sites/tutorial2program/files/graph-bfs-step-1.jpg)

Next, we visit the element at the front of queue i.e. 1 and go to its adjacent nodes. Since 0 has already been visited, we visit 2 instead.





![visit the first neighbour of start node 0, which is 1](https://cdn.programiz.com/sites/tutorial2program/files/graph-bfs-step-2.jpg)

Vertex 2 has an unvisited adjacent vertex in 4, so we add that to the back of the queue and visit 3, which is at the front of the queue.

![visit 2 which was added to queue earlier to add its neighbours](https://cdn.programiz.com/sites/tutorial2program/files/graph-bfs-step-3.jpg)

![visit ](https://cdn.programiz.com/sites/tutorial2program/files/graph-bfs-step-4.jpg)

 

Only 4 remains in the queue since the only adjacent node of 3 i.e. 0 is already visited. We visit it.

![visit last remaining item in stack to check if it has unvisited neighbours](https://cdn.programiz.com/sites/tutorial2program/files/graph-bfs-step-5.jpg)

Since the queue is empty, we have completed the Depth First Traversal of the graph.



[wiki](https://en.wikipedia.org/wiki/Breadth-first_search)

# BFS

bfs和dfs很像，不过在图的便利中，bfs先从root节点开始，在遍历第一层，如何第二层，一直从后。

# 代码

```python
import collections

def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]} 
    breadth_first_search(graph, 0)
```

