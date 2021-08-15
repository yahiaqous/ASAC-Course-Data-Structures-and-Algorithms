from trees.trees import BinaryTree,Node

# CC15
def test_instantiate_an_empty_tree():
  binary_tree = BinaryTree
  assert binary_tree

def test_instantiate_a_tree_with_a_single_root_node():
  binary_tree = BinaryTree
  node1 = Node('A')
  binary_tree.root=node1
  assert binary_tree.root.value == 'A'


def test_add_a_left_child_and_righy_child_to_a_single_root_node():
  binary_tree = BinaryTree
  node1 = Node('A')
  node2 = Node('B')
  node3 = Node('C')
  binary_tree.root=node1
  node1.left = node2
  node1.right = node3
  assert node1.left.value == 'B'
  assert node1.right.value == 'C'

def test_return_a_collection_from_a_preorder_traversal():
  binary_tree=BinaryTree()
  node1 = Node('A')
  node2 = Node('B')
  node3 = Node('C')
  node4 = Node('D')
  node5 = Node('E')
  node6 = Node('F')
  binary_tree.root=node1
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.left = node6
  pre_order = binary_tree.pre_order()
  assert pre_order == ['A', 'B', 'D', 'E', 'C', 'F']

def test_return_a_collection_from_a_inorder_traversal():
  binary_tree=BinaryTree()
  node1 = Node('A')
  node2 = Node('B')
  node3 = Node('C')
  node4 = Node('D')
  node5 = Node('E')
  node6 = Node('F')
  binary_tree.root=node1
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.left = node6
  in_order = binary_tree.in_order()
  assert in_order == ['D', 'B', 'E', 'A', 'F', 'C']

def test_return_a_collection_from_a_postorder_traversal():
  binary_tree=BinaryTree()
  node1 = Node('A')
  node2 = Node('B')
  node3 = Node('C')
  node4 = Node('D')
  node5 = Node('E')
  node6 = Node('F')
  binary_tree.root=node1
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.left = node6
  post_order = binary_tree.post_order()
  assert post_order == ['D', 'E', 'B', 'F', 'C', 'A']


