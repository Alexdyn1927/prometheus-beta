class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to help with Kruskal's algorithm.
    
    This class helps efficiently determine if adding an edge would create a cycle
    and supports merging sets of vertices.
    """
    def __init__(self, vertices):
        """
        Initialize the disjoint set.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item):
        """
        Find the root of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Merge two sets using union by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if merge was successful, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(graph):
    """
    Find the Minimum Spanning Tree using Kruskal's Algorithm.
    
    :param graph: A list of edges, where each edge is a tuple (weight, u, v)
    :return: List of edges in the minimum spanning tree
    :raises ValueError: If the graph is None, empty, or not a valid graph representation
    """
    # Input validation
    if graph is None or len(graph) == 0:
        raise ValueError("Graph cannot be None or empty")
    
    # Determine the number of vertices
    vertices = max(max(u, v) for _, u, v in graph) + 1
    
    # Sort edges by weight
    sorted_edges = sorted(graph, key=lambda x: x[0])
    
    # Initialize Disjoint Set
    ds = DisjointSet(vertices)
    
    # Minimum Spanning Tree edges
    mst_edges = []
    
    # Kruskal's algorithm
    for weight, u, v in sorted_edges:
        # If adding this edge doesn't create a cycle, add it to MST
        if ds.union(u, v):
            mst_edges.append((weight, u, v))
        
        # Stop when we have vertices-1 edges (complete MST)
        if len(mst_edges) == vertices - 1:
            break
    
    return mst_edges