import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_basic():
    """Test basic Disjoint Set operations."""
    ds = DisjointSet(5)
    
    # Initially, each vertex should be in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union of vertices
    assert ds.union(0, 1) == True
    assert ds.find(0) == ds.find(1)
    
    # Trying to union already connected vertices
    assert ds.union(0, 1) == False

def test_kruskal_mst_basic():
    """Test Kruskal's algorithm with a simple graph."""
    # Graph with 4 vertices: (weight, u, v)
    graph = [
        (1, 0, 1),
        (4, 0, 2),
        (3, 1, 2),
        (2, 1, 3),
        (5, 2, 3)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected edges in the MST and their total weight
    expected_edges = [(1, 0, 1), (2, 1, 3), (3, 1, 2)]
    expected_weight_sum = 6
    
    # Check the edges and total weight
    assert len(mst) == 3  # vertices-1 edges
    assert set(mst) == set(expected_edges)
    assert sum(edge[0] for edge in mst) == expected_weight_sum

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm with a disconnected graph."""
    graph = [
        (1, 0, 1),
        (2, 2, 3),
        (3, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Should still return a valid MST
    assert len(mst) == 2  # Some vertices will be disconnected

def test_kruskal_mst_error_handling():
    """Test error handling for invalid inputs."""
    # Test None input
    with pytest.raises(ValueError, match="Graph cannot be None or empty"):
        kruskal_mst(None)
    
    # Test empty graph
    with pytest.raises(ValueError, match="Graph cannot be None or empty"):
        kruskal_mst([])

def test_kruskal_mst_complex_graph():
    """Test Kruskal's algorithm with a more complex graph."""
    graph = [
        (2, 0, 1),
        (3, 0, 2),
        (4, 1, 2),
        (5, 1, 3),
        (6, 2, 3),
        (7, 2, 4),
        (8, 3, 4)
    ]
    
    mst = kruskal_mst(graph)
    
    # Ensure we have vertices-1 edges
    assert len(mst) == 4
    
    # Check total minimum weight
    assert sum(edge[0] for edge in mst) == 15