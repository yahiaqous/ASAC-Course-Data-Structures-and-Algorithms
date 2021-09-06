from hash_table.hash_table import HashTable, repeated_word, tree_intersection
from hash_table.trees import BinaryTree, Node

# CC30
def test_adding_a_key_and_value_to_hashtable():
  hash_table = HashTable()
  hash_table.add('yahia','24')
  assert hash_table.get('yahia') == '24'

def test_retrieving_based_on_a_key_returns_the_value_stored():
  hash_table = HashTable()
  hash_table.add('yahia','24')
  assert hash_table.get('yahia') == '24'

def test_returns_null_for_a_key_that_does_not_exist_in_the_hashtable():
  hash_table = HashTable()
  assert hash_table.get('test') == None

def test_handle_a_collision_within_the_hashtable():
  hash_table = HashTable()
  hash_table.add('yahia','24')
  hash_table.add('yaiha','30')
  print(hash_table.contains('yahia'))
  print(hash_table.contains('yaiha'))

def test_retrieve_a_value_from_a_bucket_within_the_hashtable_that_has_a_collision():
  hash_table = HashTable()
  hash_table.add('yahia','24')
  hash_table.add('yaiha','30')
  assert hash_table.get('yahia') == '24'
  assert hash_table.get('yaiha') == '30'

def test_hash_a_key_to_an_in_range_value():
  hash_table = HashTable()
  assert hash_table.hash('8000')< hash_table.size

# CC31
def test_repeated_word():
  assert repeated_word("Once upon a time, there was a brave princess who...") == 'a'
  assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == 'it'
  assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == 'summer'

# CC32
def test_tree_intersection():
  node1 = Node(150)
  node2 = Node(100)
  node3 = Node(250)
  node4 = Node(75)
  node5 = Node(160)
  node6 = Node(200)
  node7 = Node(350)
  node8 = Node(125)
  node9 = Node(175)
  node10 = Node(300)
  node11 = Node(500)
  binary_tree1=BinaryTree()
  binary_tree1.root=node1
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.left = node6
  node3.right = node7
  node5.left = node8
  node5.right = node9
  node7.left = node10
  node7.right = node11

  node_one = Node(42)
  node_two = Node(100)
  node_three = Node(600)
  node_four = Node(15)
  node_five = Node(160)
  node_six = Node(200)
  node_seven = Node(350)
  node_eight = Node(125)
  node_nine = Node(175)
  node_ten = Node(4)
  node_eleven = Node(500)
  binary_tree2=BinaryTree()
  binary_tree2.root=node_one
  node_one.left = node_two
  node_one.right = node_three
  node_two.left = node_four
  node_two.right = node_five
  node_three.left = node_six
  node_three.right = node_seven
  node_five.left = node_eight
  node_five.right = node_nine
  node_seven.left = node_ten
  node_seven.right = node_eleven

  assert tree_intersection(binary_tree1,binary_tree2) == [100, 160, 125, 175, 200, 350, 500]
