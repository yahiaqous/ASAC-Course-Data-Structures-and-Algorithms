class Node:
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return str(self.value)


class Edge:
  def __init__(self, node, weight=1):
    self.node = node
    self.weight = weight

  def __str__(self):
    return str(self.weight)


class Graph:
  def __init__(self):
    self._adjacency_list = {}

  def __str__(self):
    string = '{'
    for i in self._adjacency_list:
      string += f'{str(i)}:['
      for j in self._adjacency_list[i]:
        string += f'{str(j.node)},'
      string += f'], '
    string += '}'
    return string

# CC35
  def add_node(self, node:Node):
    """
    Adds a node to the graph
    arguments -->    node
    """
    self._adjacency_list[node]=[]
    return node

  def add_edge(self, node1, node2, weight=1):
    """Adds an edge to our graph"""
    edge = Edge(node2,weight)
    self._adjacency_list[node1].append(edge)

  def get_nodes(self):
    list = []
    for i in self._adjacency_list:
      list.append(str(i))
    return list

  def get_neighbors(self,node):
    list = []
    for i in self._adjacency_list[node]:
      dictionary ={}
      dictionary[i.node.value]=i.weight
      list.append(dictionary)
    return list

  def size(self):
    return len(self._adjacency_list)



if __name__=='__main__':
# CC35
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

  graph.add_edge(node_a,node_c,1)
  graph.add_edge(node_a,node_d,2)
  graph.add_edge(node_b,node_c,3)
  graph.add_edge(node_b,node_f,4)
  graph.add_edge(node_c,node_a,1)
  graph.add_edge(node_c,node_b,3)
  graph.add_edge(node_c,node_e,5)
  graph.add_edge(node_d,node_a,2)
  graph.add_edge(node_d,node_e,6)
  graph.add_edge(node_e,node_c,5)
  graph.add_edge(node_e,node_d,6)
  graph.add_edge(node_e,node_f,7)
  graph.add_edge(node_f,node_b,4)
  graph.add_edge(node_f,node_e,7)

  print(graph)
  print(graph.get_nodes())
  print(graph.get_neighbors(node_a))
  print(graph.get_neighbors(node_b))
  print(graph.get_neighbors(node_c))
  print(graph.get_neighbors(node_d))
  print(graph.get_neighbors(node_e))
  print(graph.get_neighbors(node_f))
  print(graph.size())
