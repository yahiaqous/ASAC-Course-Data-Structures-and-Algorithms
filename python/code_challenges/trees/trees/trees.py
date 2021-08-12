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
  pre_order_output = []

  def pre_order(self,root):
    self.pre_order_output.append(root.value)
    if (root.left): self.pre_order(root.left)
    if (root.right): self.pre_order(root.right)
    return self.pre_order_output


  in_order_output = []

  def in_order(self,root):
    if root.left: self.in_order(root.left)
    self.in_order_output.append(root.value)
    if root.right: self.in_order(root.right)
    return self.in_order_output

  post_order_output = []

  def post_order(self,root):
    if root.left: self.post_order(root.left)
    if root.right: self.post_order(root.right)
    self.post_order_output.append(root.value)
    return self.post_order_output

class BinarySearchTree(BinaryTree):
  def __init__(self, node=None):
      BinaryTree.__init__(self,node=None)

  def add(self,value,root):
    node = Node(value)

    if value <= root.value:
      if root.left: self.add(value,root.left)
      else: root.left = node

    elif value >= root.value:
      if root.right: self.add(value,root.right)
      else: root.right = node

  compare = 0
  def contains(self,value,root):
    self.compare = value

    if self.compare == root.value: self.compare = True

    elif self.compare < root.value:
      if root.left: self.contains(self.compare,root.left)
      else: return False

    elif value > root.value:
      if root.right: self.contains(self.compare,root.right)
      else: return False

    if self.compare == True: return True
    else: return False




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
  # binary_tree=BinaryTree()
  # binary_tree.root=node1
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.left = node6
  node3.right = node7
  node5.left = node8
  node5.right = node9
  node7.right = node10
  # print (binary_tree.pre_order(node1))
  # print (binary_tree.in_order(node1))
  # print (binary_tree.post_order(node1))
  binary_search_tree = BinarySearchTree()
  binary_search_tree.root=node1
  print (binary_search_tree.pre_order(node1))
  binary_search_tree.add(50,node1)
  print (binary_search_tree.pre_order(node1))
  print(binary_search_tree.contains(50,node1))

