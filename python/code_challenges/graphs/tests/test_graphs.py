from graphs.graphs import Node, Edge, Graph, business_trip

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

# CC37
def test_bussiness_trip():
  node_pandora = Node('pandora')
  node_arendelle = Node('arendelle')
  node_metroville = Node('metroville')
  node_monstropolis = Node('monstropolis')
  node_naboo = Node('naboo')
  node_narnia = Node('narnia')

  trip = Graph()

  trip.add_node(node_pandora)
  trip.add_node(node_arendelle)
  trip.add_node(node_metroville)
  trip.add_node(node_monstropolis)
  trip.add_node(node_naboo)
  trip.add_node(node_narnia)

  trip.add_edge(node_pandora,node_arendelle,150)
  trip.add_edge(node_pandora,node_metroville,82)
  trip.add_edge(node_arendelle,node_pandora,150)
  trip.add_edge(node_arendelle,node_metroville,99)
  trip.add_edge(node_arendelle,node_monstropolis,42)
  trip.add_edge(node_metroville,node_pandora,82)
  trip.add_edge(node_metroville,node_arendelle,99)
  trip.add_edge(node_metroville,node_monstropolis,105)
  trip.add_edge(node_metroville,node_naboo,26)
  trip.add_edge(node_metroville,node_narnia,37)
  trip.add_edge(node_monstropolis,node_arendelle,42)
  trip.add_edge(node_monstropolis,node_metroville,105)
  trip.add_edge(node_monstropolis,node_naboo,73)
  trip.add_edge(node_naboo,node_monstropolis,73)
  trip.add_edge(node_naboo,node_metroville,26)
  trip.add_edge(node_naboo,node_narnia,250)
  trip.add_edge(node_narnia,node_metroville,37)
  trip.add_edge(node_narnia,node_naboo,250)

  assert business_trip(trip,['Metroville', 'Pandora' ]) == 82
  assert business_trip(trip,['Arendelle', 'Monstropolis', 'Naboo']) == 115
  assert business_trip(trip,['Naboo', 'Pandora']) == None
  assert business_trip(trip,['Narnia', 'Arendelle', 'Naboo']) == None
