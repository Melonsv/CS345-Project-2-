import random
import sys
from collections import deque
from queue import PriorityQueue
import math


class Node:
    def __init__(self, value):
        self.value = value


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
        self._DFSRec(graph, start_node, final_node)
        if self.visited[0] == start_node and self.visited[-1] == final_node:
            return self.visited
        else:
            return

    def _DFSRec(self, graph, start_node, final_node):
        if start_node == final_node:
            self.visited.append(start_node)
            return
        self.visited.append(start_node)
        for edge in graph.adjacency_list[start_node]:
            if edge not in self.visited and final_node not in self.visited:
                self._DFSRec(graph, edge, final_node)

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
                self._BFTRec(graph, queue)
        return self.visited

    def _BFTRec(self, graph, queue):
        if queue:
            cur = queue.popleft()
            for edge in graph.adjacency_list[cur]:
                if edge not in self.visited:
                    self.visited.append(edge)
                    queue.append(edge)
            self._BFTRec(graph, queue)

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
                self._mDFS(graph, vertex, stack)
        stack.reverse()
        return stack

    def _mDFS(self, graph, vertex, stack):
        self.visited.append(vertex)
        for neighbor in graph.adjacency_list[vertex]:
            if neighbor not in self.visited:
                self._mDFS(graph, neighbor, stack)
        stack.append(vertex)


class WeightedGraph(DirectedGraph):
    def addNode(self, value):
        node = Node(value)
        if node.value not in self.adjacency_list:
            self.adjacency_list[node.value] = {}

    def addWeightedEdge(self, first_node, second_node, weight):
        if first_node in self.adjacency_list and second_node in self.adjacency_list:
            self.adjacency_list[first_node][second_node] = weight


# Part 1-3
"""def createRandomUnweightedGraphIter(num_nodes):
    graph = Graph()
    for num in range(num_nodes):
        value = random.randint(0, num_nodes)
        while value in graph.adjacency_list:
            value = random.randint(0, num_nodes)
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        graph.addUndirectedEdge(node_list[index], node_list[random.randint(0, num_nodes - 1)])
    return graph


def createLinkedList(num_nodes):
    graph = Graph()
    for num in range(num_nodes):
        value = random.randint(0, num_nodes)
        while value in graph.adjacency_list:
            value = random.randint(0, num_nodes)
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        if index != num_nodes - 1:
            graph.addDirectedEdge(node_list[index], node_list[index + 1])
    return graph


def BFTRecLinkedList(graph):
    search = GraphSearch()
    return search.BFTRec(graph)


def BFTIterLinkedList(graph):
    search = GraphSearch()
    return search.BFTIter(graph)



# This is used to increase the recursion limit so one can see execution of different sized graphs
sys.setrecursionlimit(10**6)
graph = createRandomUnweightedGraphIter(10)
search = GraphSearch()
node_set = graph.getAllNodes()
node_list = list(graph.getAllNodes())
print("Random Unweighted Graph", graph.adjacency_list)
print("Set of Nodes:", node_set)
print("DFSRec:", search.DFSRec(graph, node_list[0], node_list[-1]))
print("DFSIter:", search.DFSIter(graph, node_list[0], node_list[-1]))
print("BFTRec:", search.BFTRec(graph))
print("BFTIter", search.BFTIter(graph))

graph = createLinkedList(10000)
print("\n\nRandom Linked List", graph.adjacency_list)
print("BFTRecLinkedList:", BFTRecLinkedList(graph))
print("BFTIterLinkedList", BFTIterLinkedList(graph))"""


# Part 4-7
def createRandomDAGIter(num_nodes):
    graph = DirectedGraph()
    search = GraphSearch()
    for num in range(num_nodes):
        value = random.randint(0, num_nodes)
        while value in graph.adjacency_list:
            value = random.randint(0, num_nodes)
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        first_index = random.randint(0, num_nodes - 1)
        second_index = random.randint(0, num_nodes - 1)
        while node_list[second_index] == node_list[first_index]:
            second_index = random.randint(0, num_nodes - 1)
        if random.randrange(101) > 5:
            if search.DFSIter(graph, node_list[second_index], node_list[first_index]):
                continue
            else:
                graph.addDirectedEdge(node_list[first_index], node_list[second_index])
    return graph


def createRandomCompleteWeightedGraph(num_nodes):
    graph = WeightedGraph()
    for num in range(num_nodes):
        value = random.randint(0, num_nodes)
        while value in graph.adjacency_list:
            value = random.randint(0, num_nodes)
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        for second_index in range(num_nodes):
            if index != second_index:
                graph.addWeightedEdge(node_list[index], node_list[second_index], random.randint(1, num_nodes))
    return graph


def createWeightedLinkedList(num_nodes):
    graph = WeightedGraph()
    for num in range(num_nodes):
        value = random.randint(0, num_nodes)
        while value in graph.adjacency_list:
            value = random.randint(0, num_nodes)
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        if index != num_nodes - 1:
            graph.addWeightedEdge(node_list[index], node_list[index + 1], 1)
    return graph


def dijkstras(graph, node):
    distance = {node: math.inf for node in graph.adjacency_list}
    queue = PriorityQueue()
    for vertex in graph.adjacency_list:
        if vertex is not node:
            queue.put(vertex)
            distance[node] = 0
    while queue:
        cur = queue.get()
        for vertex in graph.adjacency_list[cur]:
            temp_distance = distance[cur] + graph.adjacency_list[cur][vertex]
            if temp_distance < distance[vertex]:
                distance[vertex] = temp_distance
    return distance


g = createRandomCompleteWeightedGraph(5)
print(g.adjacency_list)
dijkstras(g, 0)

