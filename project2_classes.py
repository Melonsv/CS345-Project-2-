from collections import deque


class Node:
    def __init__(self, value):
        self.value = value


class GridNode(Node):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        super().__init__(value)


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addNode(self, value):
        node = Node(value)
        if node.value not in self.adjacency_list:
            self.adjacency_list[node.value] = []

    def addUndirectedEdge(self, first_node, second_node):
        if first_node in self.adjacency_list and second_node in self.adjacency_list:
            if second_node not in self.adjacency_list[first_node]:
                self.adjacency_list[first_node].append(second_node)
            if first_node not in self.adjacency_list[second_node]:
                self.adjacency_list[second_node].append(first_node)

    def addDirectedEdge(self, first_node, second_node):
        if first_node in self.adjacency_list and second_node in self.adjacency_list:
            self.adjacency_list[first_node].append(second_node)

    def removeUndirectedEdge(self, first_node, second_node):
        if first_node in self.adjacency_list and second_node in self.adjacency_list:
            if second_node in self.adjacency_list[first_node] and first_node in self.adjacency_list[second_node]:
                self.adjacency_list[first_node].remove(second_node)
                self.adjacency_list[second_node].remove(first_node)

    def getAllNodes(self):
        return set(self.adjacency_list)


class GraphSearch:
    def __init__(self):
        self.visited = []

    def DFSRec(self, graph, start_node, final_node):
        self.visited = []
        self._DFSRecHelper(graph, start_node, final_node)
        if self.visited[0] == start_node and self.visited[-1] == final_node:
            return self.visited
        else:
            return

    def _DFSRecHelper(self, graph, start_node, final_node):
        if start_node == final_node:
            self.visited.append(start_node)
            return
        self.visited.append(start_node)
        for edge in graph.adjacency_list[start_node]:
            if edge not in self.visited and final_node not in self.visited:
                self._DFSRecHelper(graph, edge, final_node)

    def DFSIter(self, graph, start_node, final_node):
        stack = []
        if start_node not in self.visited:
            self.visited.append(start_node)
            stack.append(start_node)
            while stack:
                cur = stack.pop()
                if start_node == final_node:
                    self.visited.append(start_node)
                    return
                for edge in graph.adjacency_list[cur]:
                    if edge not in self.visited and final_node not in self.visited:
                        self.visited.append(edge)
                        stack.append(edge)
        if self.visited[0] == start_node and self.visited[-1] == final_node:
            return self.visited
        else:
            return

    def BFTRec(self, graph):
        self.visited = []
        queue = deque()
        for vertex in graph.adjacency_list:
            if vertex not in self.visited:
                self.visited.append(vertex)
                queue.append(vertex)
                self._BFTRecHelper(graph, queue)
        return self.visited

    def _BFTRecHelper(self, graph, queue):
        if queue:
            cur = queue.popleft()
            for edge in graph.adjacency_list[cur]:
                if edge not in self.visited:
                    self.visited.append(edge)
                    queue.append(edge)
            self._BFTRecHelper(graph, queue)

    def BFTIter(self, graph):
        self.visited = []
        queue = deque()
        for vertex in graph.adjacency_list:
            if vertex not in self.visited:
                self.visited.append(vertex)
                queue.append(vertex)
                while queue:
                    cur = queue.popleft()
                    for edge in graph.adjacency_list[cur]:
                        if edge not in self.visited:
                            self.visited.append(edge)
                            queue.append(edge)
        return self.visited


class DirectedGraph(Graph):
    def removeDirectedEdge(self, first_node, second_node):
        if first_node in self.adjacency_list and second_node in self.adjacency_list:
            self.adjacency_list[first_node].remove(second_node)

    def addDirectedEdge(self, first_node, second_node):
        if first_node in self.adjacency_list and second_node in self.adjacency_list:
            if first_node not in self.adjacency_list[second_node] and first_node != second_node:
                self.adjacency_list[first_node].append(second_node)


class TopSort:
    def __init__(self):
        self.visited = []

    def Kahns(self, graph):
        in_degree = {node: 0 for node in graph.adjacency_list}
        output = []
        queue = deque()
        for node in graph.adjacency_list:
            for vertex in graph.adjacency_list[node]:
                in_degree[vertex] += 1
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)
        while queue:
            cur = queue.popleft()
            output.append(cur)
            for vertex in graph.adjacency_list[cur]:
                in_degree[vertex] -= 1
                if in_degree[vertex] == 0:
                    queue.append(vertex)
        return output

    def mDFS(self, graph):
        self.visited = []
        stack = []
        for vertex in graph.adjacency_list:
            if vertex not in self.visited:
                self._mDFSHelper(graph, vertex, stack)
        stack.reverse()
        return stack

    def _mDFSHelper(self, graph, vertex, stack):
        self.visited.append(vertex)
        for neighbor in graph.adjacency_list[vertex]:
            if neighbor not in self.visited:
                self._mDFSHelper(graph, neighbor, stack)
        stack.append(vertex)


class WeightedGraph(DirectedGraph):
    def addNode(self, value):
        node = Node(value)
        if node.value not in self.adjacency_list:
            self.adjacency_list[node.value] = {}

    def addWeightedEdge(self, first_node, second_node, weight):
        if first_node in self.adjacency_list and second_node in self.adjacency_list:
            self.adjacency_list[first_node][second_node] = weight


class GridGraph(Graph):
    def addGridNode(self, x, y, node_value):
        node = GridNode(x, y, node_value)
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def addUndirectedEdge(self, first_node, second_node):
        if first_node in self.adjacency_list and second_node in self.adjacency_list:
            if first_node.x + 1 == second_node.x or first_node.x - 1 == second_node.x or \
                    first_node.y - 1 == second_node.y or first_node.y + 1 == second_node.y:
                if second_node not in self.adjacency_list[first_node]:
                    self.adjacency_list[first_node].append(second_node)
                if first_node not in self.adjacency_list[second_node]:
                    self.adjacency_list[second_node].append(first_node)
