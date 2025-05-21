import unittest
import sys
import os

# Ana dizini Python yoluna ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Doğru import
from codes.shortest_path import dijkstra

class TestShortestPath(unittest.TestCase):
    def test_dijkstra(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }
        result = dijkstra(graph, 'A')
        self.assertEqual(result['A'], 0)
        self.assertEqual(result['B'], 1)
        self.assertEqual(result['C'], 3)
        self.assertEqual(result['D'], 4)
    
    # Diğer test metodlarınız...

if __name__ == '__main__':
    unittest.main()
