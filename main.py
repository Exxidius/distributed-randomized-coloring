import sys
import argparse
import random

def randomizedColoring(graph, degree):
    uncolored_vertices = list(graph.keys())
    permanent_colors = dict() 
    color_nums = degree + 1 
    colors_used = set() 

    n_iterations = 0
    while(len(uncolored_vertices) > 0):
        candidate_colors = dict()
        for v in uncolored_vertices:
            possible_colors = possibleColors(graph, permanent_colors,
                                             v, color_nums)
            candidate_colors[v] = random.sample(possible_colors, 1)

        for v in candidate_colors:
            if(permanentlyColor(graph, candidate_colors, v)):
                permanent_colors[v] = candidate_colors[v]
                uncolored_vertices.remove(v)
                colors_used.add(candidate_colors[v][0])
        n_iterations += 1

    return permanent_colors, n_iterations, len(colors_used)

def permanentlyColor(graph, candidate_colors, vertex):
    desired_color = candidate_colors[vertex]
    for nb in graph[vertex]:
        if(nb in candidate_colors and desired_color == candidate_colors[nb]):
            return False
    return True

def possibleColors(graph, colored_vertices, vertex, number_colors):
    colors = list(range(1, number_colors + 1))
    for nb in graph[vertex]:
        if(nb in colored_vertices and colored_vertices[nb][0] in colors):
            colors.remove(colored_vertices[nb][0])
    return colors

def createRandomGraph(num_vertices, num_edges):
    if(num_edges > num_vertices * (num_vertices - 1) / 2):
        print('Multigraphs not allowed - decrease number of edges!')
        exit(-1)

    graph = { }
    act_edges = 0
    
    for i in range(1, num_vertices + 1): graph[i] = list()
    
    while(act_edges < num_edges):
        edge = random.sample(list(range(1, num_vertices + 1)), 2)
        if(edge[0] == edge[1]): continue
        if(edge[1] not in graph[edge[0]]):
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            act_edges += 1

    degree = max([len(val) for val in graph.values()])
    return graph, degree

def testAlgorithm(graph, coloring):
    for v in list(graph.keys()):
        color_v = coloring[v][0]
        for nb in graph[v]:
            color_nb = coloring[nb][0]
            if(color_v == color_nb):
                return False
    return True

def printUsage():
    print("Usage: python3 main.py print_result num_vertices num_edges")
    print("     print_result: bool, print the final coloring and graph")
    print("     num_vertices: int, create a graph with num_vertices vertices")
    print("     num_edges:  int, create a graph wiht num_edges edges")

def printStatistics(degree, n_iterations, num_used):
    colors_num = degree + 1
    print(f'Degree of graph is: {degree}')
    print(f'Number of colors possible: {colors_num}')
    print(f'Number of colors used: {num_used}')
    print(f'Computation took {n_iterations} iterations')

def parseArguments():
    parser = argparse.ArgumentParser(description="Randomized Distributed Algorithm")
    parser.add_argument('-g', '--pgraph', default=False, action='store_true',
                        help="Print graph")
    parser.add_argument('-c', '--pcoloring', default=False, action='store_true',
                        help="Print coloring")
    parser.add_argument('-v', '--vertices', default=300, type=int,
                        help="Number of vertices")
    parser.add_argument('-e', '--edges', default=300, type=int,
                        help="Number of edges")

    return parser.parse_args()

def main():
    args = parseArguments()
    graph, degree = createRandomGraph(args.vertices, args.edges)
    coloring, n_iterations, num_used = randomizedColoring(graph, degree)

    if(testAlgorithm(graph, coloring)):
        print('Coloring succeeded!')
    else:
        print('No valid coloring found!')

    printStatistics(degree, n_iterations, num_used)
    if(args.pgraph):
        print(f'Graph: {graph}')
    if(args.pcoloring):
        print(f'Coloring: {coloring}')

if __name__ == "__main__":
    main()
