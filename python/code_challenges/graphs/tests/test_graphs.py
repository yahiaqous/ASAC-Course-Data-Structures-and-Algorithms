from graphs.graphs import Node, Edge, Graph

# CC35
def test_node_can_be_successfully_added_to_the_graph():
  node_a = Node('a')
  graph = Graph()
  graph.add_node(node_a)
  assert node_a in graph._adjacency_list
  assert graph._adjacency_list[node_a] == []

def test_edge_can_be_successfully_added_to_the_graph():
  node_a = Node('a')
  node_b = Node('b')
  graph = Graph()
  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_edge(node_a,node_b,1)
  assert graph._adjacency_list[node_a][0].node == node_b

def test_a_collection_of_all_nodes_can_be_properly_retrieved_from_the_graph():
  node_a = Node('a')
  node_b = Node('b')
  node_c = Node('c')
  node_d = Node('d')
  node_e = Node('e')
  node_f = Node('f')
  graph = Graph()
  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_node(node_c)
  graph.add_node(node_d)
  graph.add_node(node_e)
  graph.add_node(node_f)
  assert graph.get_nodes() == ['a', 'b', 'c', 'd', 'e', 'f']

def test_all_appropriate_neighbors_can_be_retrieved_from_the_graph():
  node_a = Node('a')
  node_b = Node('b')
  node_c = Node('c')
  graph = Graph()
  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_node(node_c)
  graph.add_edge(node_a,node_b,1)
  graph.add_edge(node_a,node_c,2)
  assert graph.get_neighbors(node_a) == [{'b': 1}, {'c': 2}]

def test_neighbors_are_returned_with_the_weight_between_nodes_included():
  node_a = Node('a')
  node_b = Node('b')
  node_c = Node('c')
  graph = Graph()
  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_node(node_c)
  graph.add_edge(node_a,node_b,1)
  graph.add_edge(node_a,node_c,2)
  assert graph.get_neighbors(node_a) == [{'b': 1}, {'c': 2}]

def test_the_proper_size_is_returned_representing_the_number_of_nodes_in_the_graph():
  node_a = Node('a')
  node_b = Node('b')
  node_c = Node('c')
  node_d = Node('d')
  node_e = Node('e')
  node_f = Node('f')
  graph = Graph()
  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_node(node_c)
  graph.add_node(node_d)
  graph.add_node(node_e)
  graph.add_node(node_f)
  assert graph.size() == 6

def test_a_graph_with_only_one_node_and_edge_can_be_properly_returned():
  node_a = Node('a')
  graph = Graph()
  graph.add_node(node_a)
  graph.add_edge(node_a,node_a,1)
  assert graph._adjacency_list


def test_an_empty_graph_properly_returns_null():
  graph = Graph()
  assert graph._adjacency_list == {}
