import pytest
from src.boruvka_mst import boruvka_mst

def test_empty_graph():
    assert boruvka_mst(0, []) == []
    assert boruvka_mst(5, []) == []

def test_single_vertex():
    assert boruvka_mst(1, []) == []

def test_simple_graph():
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (1, 2, 15),
        (1, 3, 5),
        (2, 3, 4)
    ]
    mst = boruvka_mst(4, edges)
    
    # Validate the result
    assert len(mst) == 3  # A tree with n vertices has n-1 edges
    assert set((u, v) for u, v, _ in mst) == {(0, 2), (1, 3), (2, 3)}

def test_fully_connected_graph():
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 2, 15),
        (1, 3, 4),
        (2, 3, 9)
    ]
    mst = boruvka_mst(4, edges)
    
    # Validate the result
    assert len(mst) == 3
    total_weight = sum(weight for _, _, weight in mst)
    assert total_weight == 15  # Expected total weight of MST

def test_disconnected_graph():
    edges = [
        (0, 1, 10),
        (2, 3, 15)
    ]
    # This case cannot form a complete MST
    mst = boruvka_mst(4, edges)
    assert len(mst) == 0

def test_large_graph():
    # A more complex graph to test scalability
    edges = [
        (0, 1, 4), (0, 7, 8),
        (1, 2, 8), (1, 7, 11),
        (2, 3, 7), (2, 8, 2),
        (2, 5, 4), (3, 4, 9),
        (3, 5, 14), (4, 5, 10),
        (5, 6, 2), (6, 7, 1),
        (6, 8, 6), (7, 8, 7)
    ]
    mst = boruvka_mst(9, edges)
    
    # Validate the result
    assert len(mst) == 8  # A tree with 9 vertices has 8 edges
    total_weight = sum(weight for _, _, weight in mst)
    assert total_weight == 37  # Expected total weight of MST