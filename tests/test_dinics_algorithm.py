import pytest
from src.dinics_algorithm import DinicMaxFlow

def test_basic_max_flow():
    """Test a simple max flow scenario"""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {4: 10},
        4: {}
    }
    max_flow = DinicMaxFlow(graph)
    assert max_flow.max_flow(0, 4) == 19

def test_disconnected_graph():
    """Test graph with no path between source and sink"""
    graph = {
        0: {1: 10},
        1: {},
        2: {3: 5},
        3: {}
    }
    max_flow = DinicMaxFlow(graph)
    assert max_flow.max_flow(0, 3) == 0

def test_complex_graph():
    """Test a more complex flow network"""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 4, 3: 1},
        2: {3: 2},
        3: {}
    }
    max_flow = DinicMaxFlow(graph)
    assert max_flow.max_flow(0, 3) == 4

def test_invalid_source_sink():
    """Test error handling for invalid source or sink"""
    graph = {
        0: {1: 10},
        1: {}
    }
    max_flow = DinicMaxFlow(graph)
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        max_flow.max_flow(2, 1)

def test_zero_capacity_graph():
    """Test graph with zero capacities"""
    graph = {
        0: {1: 0, 2: 0},
        1: {2: 0},
        2: {}
    }
    max_flow = DinicMaxFlow(graph)
    assert max_flow.max_flow(0, 2) == 0