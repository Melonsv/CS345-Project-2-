import random
import sys
from collections import deque


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


def createRandomUnweightedGraphIter(num_nodes):
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
print("BFTIterLinkedList", BFTIterLinkedList(graph))


