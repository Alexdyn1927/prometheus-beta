from typing import List, Tuple, Dict

class DisjointSet:
    def __init__(self, vertices: int):
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item: int) -> int:
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def boruvka_mst(vertices: int, edges: List[Tuple[int, int, float]]) -> List[Tuple[int, int, float]]:
    """
    Implement Boruvka's algorithm to find the Minimum Spanning Tree (MST)
    
    Args:
        vertices (int): Number of vertices in the graph
        edges (List[Tuple[int, int, float]]): List of edges with (u, v, weight)
    
    Returns:
        List[Tuple[int, int, float]]: List of edges in the Minimum Spanning Tree
    """
    # Handle edge cases
    if vertices <= 0 or not edges:
        return []

    # Sort edges to ensure consistent behavior
    edges.sort(key=lambda x: x[2])

    # Initialize Disjoint Set data structure
    ds = DisjointSet(vertices)
    
    # Result MST edges
    mst_edges = []
    
    # Each vertex is initially in its own component
    components = vertices
    
    # Continue until we have a single component or no more edges to process
    while components > 1 and edges:
        # Track the cheapest edge for each component
        cheapest_edges = {}
        
        # Find cheapest edge connecting each component
        for u, v, weight in edges:
            set_u = ds.find(u)
            set_v = ds.find(v)
            
            if set_u != set_v:
                # Update cheapest edge for each component
                component_key = min(set_u, set_v)
                if component_key not in cheapest_edges or weight < cheapest_edges[component_key][2]:
                    cheapest_edges[component_key] = (u, v, weight)
        
        # Add cheapest edges that don't create cycles
        for edge in cheapest_edges.values():
            u, v, weight = edge
            if ds.union(u, v):
                mst_edges.append(edge)
                components -= 1
        
        # Remove the processed edges to avoid selecting them again
        edges = [edge for edge in edges if ds.find(edge[0]) != ds.find(edge[1])]
    
    return mst_edges