from queue import Queue

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
    return str(self.node)


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

# CC36
  # def breadth_first(self,node):
    result =[]
    result.append(node.value)

    current_node = node
    def walk(node):
      edge = self._adjacency_list[node]
      print(edge)
      child_node = edge[0].node.value
      for i in edge:
        child_node = i.node.value
        print(child_node)
        if child_node not in result: result.append(child_node)
        else:continue
      for i in edge:
        if i.node.value not in result: walk(i.node)
    walk(node)
    return result

  def breadth_first(self,node):
    nodes = []
    breadth = Queue()
    visited = []

    breadth.enqueue(node)
    visited.append(breadth.front)

    while breadth:
      front = breadth.dequeue()
      nodes.append(front)

      for i in nodes:
        if i not in visited:
          visited.append(i)
          breadth.enqueue(i)

    return nodes

# CC38
  def depth_first(self,node):
    result =[]
    result.append(node.value)

    def walk(node):
      edges = self._adjacency_list[node]
      for i in edges:
        child_node = i.node.value
        if child_node not in result:
          result.append(child_node)
          walk(i.node)
    walk(node)
    return result


# CC37
def business_trip(graph,array):
  cost = 0

  def walk(array):
    nonlocal cost
    start_city = array[0].lower()
    array.pop(0)
    for i in graph._adjacency_list:
      if i.value.lower() == start_city:
        start_city = i
        break

    neighbors = graph.get_neighbors(start_city)
    for i in neighbors:
      if list(i.keys())[0] == array[0].lower():
        cost += list(i.values())[0]
        if len(array)>1: walk(array)
  walk(array)
  if cost>0:return cost
  else: return None




if __name__=='__main__':
# CC35
  # node_a = Node('a')
  # node_b = Node('b')
  # node_c = Node('c')
  # node_d = Node('d')
  # node_e = Node('e')
  # node_f = Node('f')

  # graph = Graph()

  # graph.add_node(node_a)
  # graph.add_node(node_b)
  # graph.add_node(node_c)
  # graph.add_node(node_d)
  # graph.add_node(node_e)
  # graph.add_node(node_f)

  # graph.add_edge(node_a,node_c,1)
  # graph.add_edge(node_a,node_d,2)
  # graph.add_edge(node_b,node_c,3)
  # graph.add_edge(node_b,node_f,4)
  # graph.add_edge(node_c,node_a,1)
  # graph.add_edge(node_c,node_b,3)
  # graph.add_edge(node_c,node_e,5)
  # graph.add_edge(node_d,node_a,2)
  # graph.add_edge(node_d,node_e,6)
  # graph.add_edge(node_e,node_c,5)
  # graph.add_edge(node_e,node_d,6)
  # graph.add_edge(node_e,node_f,7)
  # graph.add_edge(node_f,node_b,4)
  # graph.add_edge(node_f,node_e,7)

  # print(graph)
  # print(graph._adjacency_list[node_a])
  # print(graph.get_nodes())
  # print(graph.get_neighbors(node_a))
  # print(graph.get_neighbors(node_b))
  # print(graph.get_neighbors(node_c))
  # print(graph.get_neighbors(node_d))
  # print(graph.get_neighbors(node_e))
  # print(graph.get_neighbors(node_f))
  # print(graph.size())


#CC36
  # print(graph.breadth_first(node_a))


# CC37
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

  # print(trip)
  # # print(graph._adjacency_list[node_a])
  # print(trip.get_nodes())
  # print(trip.get_neighbors(node_pandora))
  # print(trip.get_neighbors(node_arendelle))
  # print(trip.get_neighbors(node_metroville))
  # print(trip.get_neighbors(node_monstropolis))
  # print(trip.get_neighbors(node_narnia))
  # print(trip.get_neighbors(node_naboo))
  # print(trip.size())

  # print(business_trip(trip,['Metroville', 'Pandora' ]))
  # print(business_trip(trip,['Arendelle', 'Monstropolis', 'Naboo']))
  # print(business_trip(trip,['Naboo', 'Pandora']))
  # print(business_trip(trip,['Narnia', 'Arendelle', 'Naboo']))


# CC38
  node_a = Node('a')
  node_b = Node('b')
  node_c = Node('c')
  node_d = Node('d')
  node_e = Node('e')
  node_f = Node('f')
  node_g = Node('g')
  node_h = Node('h')

  graph = Graph()

  graph.add_node(node_a)
  graph.add_node(node_b)
  graph.add_node(node_c)
  graph.add_node(node_d)
  graph.add_node(node_e)
  graph.add_node(node_f)
  graph.add_node(node_g)
  graph.add_node(node_h)

  graph.add_edge(node_a,node_b)
  graph.add_edge(node_a,node_d)
  graph.add_edge(node_b,node_a)
  graph.add_edge(node_b,node_c)
  graph.add_edge(node_b,node_d)
  graph.add_edge(node_c,node_b)
  graph.add_edge(node_c,node_g)
  graph.add_edge(node_d,node_a)
  graph.add_edge(node_d,node_b)
  graph.add_edge(node_d,node_e)
  graph.add_edge(node_d,node_f)
  graph.add_edge(node_d,node_h)
  graph.add_edge(node_e,node_d)
  graph.add_edge(node_f,node_d)
  graph.add_edge(node_f,node_h)
  graph.add_edge(node_g,node_c)
  graph.add_edge(node_h,node_d)
  graph.add_edge(node_h,node_f)

  # print(graph)
  print(graph.depth_first(node_a))
