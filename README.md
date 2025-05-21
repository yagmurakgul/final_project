# final_project
# Shortest Path Algorithm Implementation

## Overview

This project implements Dijkstra's algorithm for finding the shortest path in a graph. The implementation provides an efficient solution for graph traversal problems and can be used in various applications such as route planning, network optimization, and more.

## Features

- Implementation of Dijkstra's algorithm for shortest path calculation
- Support for weighted graphs
- Comprehensive testing suite
- Well-documented code with clear examples

## Algorithm Performance

| Algorithm | Time Complexity | Space Complexity | Weighted Edges | Negative Weights |
|-----------|----------------|-----------------|----------------|-----------------|
| Dijkstra  | O(E + V log V) | O(V)            | Yes            | No              |



## Usage

Here's a simple example of how to use the shortest path algorithm:

```python
from codes.shortest_path import dijkstra

# Define a graph as an adjacency list with weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Find shortest paths from node 'A' to all other nodes
distances = dijkstra(graph, 'A')
print(distances)
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

## Project Structure

```
shortest-path/
├── codes/
│   ├── __init__.py
│   └── shortest_path.py      # Main algorithm implementation
├── tests/
│   └── test_shortestpath.py  # Unit tests
├── docs/                     # Sphinx documentation
├── .github/
│   └── workflows/
│       └── python-test.yml   # GitHub Actions configuration
├── setup.py                  # Package setup file
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## Testing

Run the tests using:

```bash
python -m unittest discover tests
```

## Documentation

For detailed documentation, please refer to the Sphinx documentation:

1. Generate the documentation:
   ```bash
   cd docs
   make html
   ```

2. View the documentation by opening `docs/build/html/index.html` in your browser.

## Requirements

- Python >= 3.6
- NumPy (if used in implementation)
- pytest (for testing)

## Future Improvements

- Add support for directed graphs
- Implement path reconstruction functionality
- Add other shortest path algorithms (Bellman-Ford, Floyd-Warshall)

## Author

Yağmur Akgül