# graph-generator
Oriented graph generator

Creates an adjacency list that represent a graph, generated by the input format.

## Usage
In the folder `test_formats` you need to add files that represent an output test
set.
With `make` command, you run the generator, that goes through each file and generates a graph from it.
In the `out` folder, you will find the test set that was generated.

## Test format
The test format is like this:
```
123         ; number of nodes
10         ; percentage of maximum number of edges (100 = complete graph)
n           ; do you want negative cost edges (y / n)
test1.in    ; output file name
```

### References
* https://www.geeksforgeeks.org/print-negative-weight-cycle-in-a-directed-graph/