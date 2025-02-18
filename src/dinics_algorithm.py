from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        """
        Initialize Dinic's algorithm with a graph represented as an adjacency list.
        
        :param graph: Dictionary representing the graph where 
                      keys are nodes and values are dictionaries of adjacent nodes and capacities
        """
        self.graph = graph
        self.nodes = list(graph.keys())
        
    def bfs(self, source: int, sink: int, level: List[int]) -> bool:
        """
        Breadth-first search to build level graph and check if sink is reachable.
        
        :param source: Source node
        :param sink: Sink node
        :param level: List to store level of each node
        :return: Boolean indicating if sink is reachable
        """
        # Reset level array
        level[:] = [-1] * len(self.nodes)
        level[source] = 0
        
        # Queue for BFS
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            for neighbor, capacity in self.graph[current].items():
                if level[neighbor] == -1 and capacity > 0:
                    level[neighbor] = level[current] + 1
                    queue.append(neighbor)
        
        return level[sink] != -1
    
    def dfs(self, current: int, sink: int, flow: int, level: List[int], 
            flow_path: List[int], graph_copy: Dict[int, Dict[int, int]]) -> int:
        """
        Depth-first search to find augmenting paths in the level graph.
        
        :param current: Current node
        :param sink: Sink node
        :param flow: Current flow
        :param level: Level of nodes
        :param flow_path: Path tracking
        :param graph_copy: Mutable copy of graph for tracking residual capacities
        :return: Augmented flow
        """
        # Reached sink
        if current == sink:
            return flow
        
        for neighbor, capacity in graph_copy[current].items():
            # Check if neighbor is in the next level and has residual capacity
            if level[neighbor] == level[current] + 1 and capacity > 0:
                # Find bottleneck flow
                curr_flow = min(flow, capacity)
                temp_flow = self.dfs(neighbor, sink, curr_flow, level, flow_path + [neighbor], graph_copy)
                
                if temp_flow > 0:
                    # Update residual graph
                    graph_copy[current][neighbor] -= temp_flow
                    graph_copy[neighbor].setdefault(current, 0)
                    graph_copy[neighbor][current] += temp_flow
                    return temp_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute maximum flow using Dinic's algorithm.
        
        :param source: Source node
        :param sink: Sink node
        :return: Maximum flow value
        """
        # Validate source and sink
        if source not in self.nodes or sink not in self.nodes:
            raise ValueError("Source or sink node not in graph")
        
        # Create a mutable copy of the graph
        graph_copy = {node: dict(edges) for node, edges in self.graph.items()}
        
        # Initialize max flow
        max_flow = 0
        
        # Level array to track node levels in BFS
        level = [-1] * len(self.nodes)
        
        # Run Dinic's algorithm
        while self.bfs(source, sink, level):
            # While augmenting paths exist
            while True:
                # Try to find an augmenting path
                path_flow = self.dfs(source, sink, float('inf'), level, [source], graph_copy)
                
                # If no augmenting path found, move to next level graph
                if path_flow == 0:
                    break
                
                # Add path flow to max flow
                max_flow += path_flow
        
        return max_flow