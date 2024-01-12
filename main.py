import sys
import random

def randomizedColoring(graph, degree):
    uncolored_vertices = list(graph.keys())
    perm_colors = dict()
    color_nums = degree + 1 

    n = 0
    while(len(uncolored_vertices) > 0):
        cand_colors = dict()
        for v in uncolored_vertices:
            possible_colors = possibleColors(graph, perm_colors, v, color_nums)
            cand_colors[v] = random.sample(possible_colors, 1)

        for v in cand_colors:
            desired_color = cand_colors[v]
            already_taken = False
            for nb in graph[v]:
                if(nb in perm_colors and desired_color == perm_colors[nb]):
                    already_taken = True
                    break
            if(not already_taken):
                perm_colors[v] = desired_color
                uncolored_vertices.remove(v)
        n += 1
    print(n)
    return perm_colors

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
    print("Usage: python3 main.py num_vertices num_edges")
    print("     num_vertices: int, create a graph with num_vertices vertices")
    print("     num_edges:  int, create a graph wiht num_edges edges")

def main():
    num_vertices = 300
    num_edges = 300
    argc = len(sys.argv)

    if argc == 2 or argc > 3:
        printUsage()
        exit(-1)

    if argc == 3:
        num_vertices = 0
        num_edges = 0
        try:
            num_vertices = int(sys.argv[1])
            num_edges = int(sys.argv[2])
        except:
            print("At least one parameter not an integer!\n")
            printUsage()
            exit(-1)

    graph, degree = createRandomGraph(num_vertices, num_edges)
    coloring = randomizedColoring(graph, degree)

    if(testAlgorithm(graph, coloring)):
        print('Coloring succeeded!')
    else:
        print('No valid coloring found!')

if __name__ == "__main__":
    main()
