class Node():
  def __init__(self,value='',left=None,right=None):
      self.value = value
      self.left = left
      self.right = right

  def __str__(self):
      return str(self.value)

class BinaryTree():
  def __init__(self, node=None):
      self.root = node

# CC15
  def pre_order(self):
    pre_order_output = []

    def walk(root):
      pre_order_output.append(root.value)
      if (root.left): walk(root.left)
      if (root.right): walk(root.right)

    walk(self.root)
    return pre_order_output

  def in_order(self):
    in_order_output = []

    def walk(root):
      if root.left: walk(root.left)
      in_order_output.append(root.value)
      if root.right: walk(root.right)

    walk(self.root)
    return in_order_output


  def post_order(self):
    post_order_output = []

    def walk(root):
      if root.left: walk(root.left)
      if root.right: walk(root.right)
      post_order_output.append(root.value)

    walk(self.root)
    return post_order_output

# CC16
  def max_value(self):
    tree = self.pre_order()
    max = self.root.value
    for i in tree:
      if i > max: max = i
    return max



class BinarySearchTree(BinaryTree):
  def __init__(self, node=None):
      BinaryTree.__init__(self,node=None)

# CC15
  def add(self,value):
    node = Node(value)
    def walk(root):

      if value <= root.value:
        if root.left: walk(root.left)
        else: root.left = node
      elif value >= root.value:
        if root.right: walk(root.right)
        else: root.right = node

    walk(self.root)

  def contains(self,value):
    compare = 0
    def walk(root):
      nonlocal compare
      compare = value

      if compare == root.value: compare = True
      elif compare < root.value:
        if root.left: walk(root.left)
        else: return False
      elif value > root.value:
        if root.right: walk(root.right)
        else: return False

      if compare == True: return True
      else: return False
    return (walk(self.root))



if __name__=="__main__":

# CC15
  node1 = Node(23)
  node2 = Node(8)
  node3 = Node(42)
  node4 = Node(4)
  node5 = Node(16)
  node6 = Node(27)
  node7 = Node(85)
  node8 = Node(15)
  node9 = Node(22)
  node10 = Node(105)
  binary_tree=BinaryTree()
  binary_tree.root=node1
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.left = node6
  node3.right = node7
  node5.left = node8
  node5.right = node9
  node7.right = node10
  print (binary_tree.pre_order())
  print (binary_tree.in_order())
  print (binary_tree.post_order())
  # binary_search_tree = BinarySearchTree()
  # binary_search_tree.root=node1
  # print (binary_search_tree.pre_order())
  # binary_search_tree.add(50)
  # print (binary_search_tree.pre_order())
  # print(binary_search_tree.contains(50))

# CC16
  print(binary_tree.max_value())
