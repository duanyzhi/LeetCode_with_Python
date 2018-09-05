# Reference

[DFS](https://www.programiz.com/dsa/graph-dfs)

# DFS algorithm



Traversal means visiting all the nodes of a [graph](https://www.programiz.com/dsa/graph). Depth first traversal or Depth first Search is a recursive algorithm for searching all the vertices of a graph or tree data structure. In this article, you will learn with the help of examples the DFS algorithm, DFS pseudocode and the code of the depth first search algorithm with implementation in C++, C, Java and Python programs.

## DFS algorithm

A standard DFS implementation puts each vertex of the graph into one of two categories:

1. Visited
2. Not Visited

The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

The DFS algorithm works as follows:

1. Start by putting any one of the graph's vertices on top of a stack.
2. Take the top item of the stack and add it to the visited list.
3. Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of stack.
4. Keep repeating steps 2 and 3 until the stack is empty.

## DFS example

Let's see how the Depth First Search algorithm works with an example. We use an undirected graph with 5 vertices.

![We start from vertex 0, the DFS algorithm starts by putting it in the Visited list and putting all its adjacent vertices in the stack.](https://cdn.programiz.com/sites/tutorial2program/files/graph-dfs-step-0.jpg)

We start from vertex 0, the DFS algorithm starts by putting it in the Visited list and putting all its adjacent vertices in the stack.

![Next, we visit the element at the top of stack i.e. 1 and go to its adjacent nodes. Since 0 has already been visited, we visit 2 instead.](https://cdn.programiz.com/sites/tutorial2program/files/graph-dfs-step-1.jpg)

Next, we visit the element at the top of stack i.e. 1 and go to its adjacent nodes. Since 0 has already been visited, we visit 2 instead



![Next, we visit the element at the top of stack i.e. 1 and go to its adjacent nodes. Since 0 has already been visited, we visit 2 instead.](https://cdn.programiz.com/sites/tutorial2program/files/graph-dfs-step-2.jpg)

Vertex 2 has an unvisited adjacent vertex in 4, so we add that to the top of the stack and visit it.

![Vertex 2 has an unvisited adjacent vertex in 4, so we add that to the top of the stack and visit it.](https://cdn.programiz.com/sites/tutorial2program/files/graph-dfs-step-3.jpg)

![Vertex 2 has an unvisited adjacent vertex in 4, so we add that to the top of the stack and visit it.](https://cdn.programiz.com/sites/tutorial2program/files/graph-dfs-step-4.jpg)

After we visit the last element 3, it doesn't have any unvisited adjacent nodes, so we have completed the Depth First Traversal of the graph.

![After we visit the last element 3, it doesn't have any unvisited adjacent nodes, so we have completed the Depth First Traversal of the graph.](https://cdn.programiz.com/sites/tutorial2program/files/graph-dfs-step-5.jpg)