import random
import numpy as np
import sys
from tqdm import tqdm
import math
import time

output_dir = 'out/'
max_cost = 1000
file_name = ''
muchii_negative = True

class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.edges = [];

    def addEdge(self, edge: Edge):
        self.edges.append(edge)

    def updateEdgeAbs(self, source, dest):
        for edge in self.edges:
                if edge.source == source and edge.dest == dest:
                    edge.weight = abs(edge.weight)


def read_input_data():
    global file_name, muchii_negative
    if (sys.argv[1] == "quiet"):
        nr_noduri = int(input())
        procent_muchii = float(input())
        muchii_negative_str = input()
        file_name = input()
    else:
        nr_noduri = int(input("Nr noduri [2, 10^5]: "))
        procent_muchii = float(input("Procent din graf complet %: "))
        muchii_negative_str = input("Muchii negative in graf y/n: ")
        file_name = input("Nume fisier iesire: ")

    nr_muchii_max = nr_noduri * (nr_noduri - 1)
    nr_muchii = int(float(procent_muchii) / 100 * nr_muchii_max)

    if (nr_muchii > 1e6):
        nr_muchii = int(1e6)

    if muchii_negative_str.startswith('n'):
        muchii_negative = False

    return Graph(nr_noduri, nr_muchii)

def write_out_file(graph: Graph):
    f = open(output_dir + file_name, "w")
    f.write(str(graph.V) + " " + str(graph.E) + "\n")

    for edge in graph.edges:
        f.write(str(edge.source) + ' ' + str(edge.dest) + ' ' + str(edge.weight) + '\n')

def generate_edges(graph: Graph):
    global muchii_negative
    maxed_sources = []
    source_dest_map = {}

    for i in tqdm(range(graph.E)):

        # select a source that has available destinations
        source = random.randint(1, graph.V)
        while source in maxed_sources:
            source = random.randint(1, graph.V)

        # get list of already used destinations for this source
        if source not in source_dest_map:
            source_dest_map[source] = []
        used_destinations = source_dest_map[source]

        # get destination
        dest = random.randint(1, graph.V)
        while dest == source or dest in used_destinations:
            dest = random.randint(1, graph.V)

        # add source dest pair to map
        used_destinations.append(dest)

        # check if source is maxed
        if len(used_destinations) == (graph.V - 1):
            maxed_sources.append(source)

        cost = int((np.random.normal(0, 2, 1)) * max_cost / 10)

        if (muchii_negative == False):
            cost = abs(cost)

        graph.edges.append(Edge(source, dest, cost))

def bellmanFordAndFix(graph: Graph, src: int, dist):
    V = graph.V
    E = graph.E

    dist = [math.inf] * (V + 1)
    dist[src] = 0;

    parent = [-1] * (V + 1)

    for i in range(1, V + 1):
        for j in range(E):
            u = graph.edges[j].source
            v = graph.edges[j].dest
            weight = graph.edges[j].weight
            if (dist[u] != math.inf and dist[u] + weight < dist[v]):
                dist[v] = dist[u] + weight
                parent[v] = u
    
    for i in range(E):
        u = graph.edges[i].source
        v = graph.edges[i].dest
        weight = graph.edges[i].weight
        if (dist[u] != math.inf and dist[u] + weight < dist[v]):
            # make sure we have at least one node from cycle
            for i in range(V):
                v = parent[v]

            # iterate through cycle and update it
            run = True
            x = v
            while run:
                source = parent[x]
                dest = x
                graph.updateEdgeAbs(source, dest)
                x = parent[x]
                if x == v:
                    run = False
            return True
    
    return False

def fixAnyNegativeCycle(graph: Graph):
    def fixAnyNegativeCycle(graph: Graph):
        print("Fixing negative cycles. This might take a while...")
    
    start_time = time.time()

    V = graph.V
    visited = [False] * (V + 1)

    dist = [None] * (V + 1)

    for i in range(1, graph.V + 1):
        if visited[i] == False:
            while bellmanFordAndFix(graph, i, dist):
                pass
        
            for j in range(1, graph.V + 1):
                if dist[j] != math.inf:
                    visited[j] = True;

    end_time = time.time()
    dif = end_time - start_time
    print("Elapsed time: " + str(dif) + " seconds")


graph = read_input_data()
print("Generating: " + file_name)
generate_edges(graph)
if muchii_negative:
    fixAnyNegativeCycle(graph)
write_out_file(graph)