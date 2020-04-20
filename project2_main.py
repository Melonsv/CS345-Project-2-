import random
import sys
from project2_classes import *
from queue import PriorityQueue
import math


def createRandomUnweightedGraphIter(num_nodes):
    graph = Graph()
    for value in random.sample(range(num_nodes), num_nodes):
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        graph.addUndirectedEdge(node_list[index], node_list[random.randint(0, num_nodes - 1)])
    return graph


def createLinkedList(num_nodes):
    graph = Graph()
    for value in random.sample(range(num_nodes), num_nodes):
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


def createRandomDAGIter(num_nodes):
    graph = DirectedGraph()
    search = GraphSearch()
    pass_percentage = 5
    percentage = 101
    for value in random.sample(range(num_nodes), num_nodes):
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        first_index = random.randint(0, num_nodes - 1)
        second_index = random.randint(0, num_nodes - 1)
        while node_list[second_index] == node_list[first_index]:
            second_index = random.randint(0, num_nodes - 1)
        if random.randrange(percentage) > pass_percentage:
            if search.DFSIter(graph, node_list[second_index], node_list[first_index]):
                continue
            else:
                graph.addDirectedEdge(node_list[first_index], node_list[second_index])
    return graph


def createRandomCompleteWeightedGraph(num_nodes):
    graph = WeightedGraph()
    for value in random.sample(range(num_nodes), num_nodes):
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        for second_index in range(num_nodes):
            if index != second_index:
                graph.addWeightedEdge(node_list[index], node_list[second_index], random.randint(1, num_nodes))
    return graph


def createWeightedLinkedList(num_nodes):
    graph = WeightedGraph()
    for value in random.sample(range(num_nodes), num_nodes):
        graph.addNode(value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes - 1):
        graph.addWeightedEdge(node_list[index], node_list[index + 1], 1)
    return graph


def dijkstras(graph, start_node):
    distance = {}
    queue = PriorityQueue()
    for node in graph.adjacency_list:
        if node != start_node:
            distance[node] = math.inf
        else:
            distance[node] = 0
        queue.put((distance[node], node))
    while queue:
        current = queue.get()
        for neighbor in graph.adjacency_list[current[1]]:
            temp_distance = distance[current[1]] + graph.adjacency_list[current[1]][neighbor]
            if temp_distance < distance[neighbor]:
                distance[neighbor] = temp_distance
    return distance


def createRandomGridGraph(num_nodes):
    graph = GridGraph()
    for x in range(num_nodes):
        for y in range(num_nodes):
            value = random.randint(0, num_nodes)
            graph.addGridNode(x, y, value)
    node_list = list(graph.getAllNodes())
    for index in range(num_nodes):
        print(node_list[index].y)
        graph.addUndirectedEdge(node_list[index], node_list[random.randint(0, num_nodes - 1)])
    return graph

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


graph = createRandomDAGIter(10000)
sort = TopSort()
print("\n\nRandom DAG", graph.adjacency_list)
print("Kahns:", sort.Kahns(graph))
print("mDFS", sort.mDFS(graph))

graph = createRandomCompleteWeightedGraph(10000)
node_list = list(graph.getAllNodes())
print("\n\nRandom Complete Weighted Graph", graph.adjacency_list)
print("dijkstras", dijkstras(graph, node_list[0]))

graph = createWeightedLinkedList(10000)
print("\n\nRandom Complete Weighted Linked List", graph.adjacency_list)

