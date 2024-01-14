# Distributed-Randomized-Coloring
Implementation of a Distributed Randomized Coloring algorithm

Version of python3 used:
Input: ``python3 --version``                                                                                               Output: ``Python 3.10.12``

Usage:
```
main.py [-h] [-g] [-c] [-v VERTICES] [-e EDGES]

Randomized Distributed Algorithm

options:
  -h, --help            show this help message and exit
  -g, --pgraph          Print graph
  -c, --pcoloring       Print coloring
  -v VERTICES, --vertices VERTICES
                        Number of vertices
  -e EDGES, --edges EDGES
                        Number of edges
```

Examples:
  - 10 vertices, 10 edges: ``python3 main.py -gc -v 10 -e 10``
  - 400 vertices, 10000 edges: ``python3 main.py -v 400 -e 10000``
  - 400 vertices, 50000 edges: ``python3 main.py -v 400 -e 50000``
  - 10 vertices, 10 edges, no graph output, no coloring output ``python3 main.py -v 10 -e 10``
  - 10 vertices, 10 edges, only coloring output  ``python3 main.py -c -v 10 -e 10``
  - 10 vertices, 10 edges, only graph output  ``python3 main.py -g -v 10 -e 10``

If the program outputs the message "Coloring succeeded!", the coloring worked (test returned true)
