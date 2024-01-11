import sys
import random

def randomizedColoring(graph):
    pass

def createRandomGraph(num_vertices, num_edges):
    graph = { 'vertices' : [], 'edges' : [] }


def testAlgorithm(graph, coloring):
    pass

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
        try:
            int(sys.argv[1])
            int(sys.argv[2])
        except:
            print("At least one parameter not an integer!\n")
            printUsage()
            exit(-1)
        num_vertices = sys.argv[1]
        num_edges = sys.argv[2]

    graph = createRandomGraph(num_vertices, num_edges)
    coloring = randomizedColoring()
    testAlgorithm(graph, coloring)

if __name__ == "__main__":
    main()
