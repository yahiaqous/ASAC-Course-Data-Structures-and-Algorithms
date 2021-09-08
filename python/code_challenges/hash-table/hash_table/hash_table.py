from linked_list import LinkedList
from trees import BinaryTree, Node

class HashTable():
  def __init__(self,size=1024):
      self.size = size
      self._buckets = [None] * size

# CC30
  def hash(self,key):
    value = 0
    if type(key)==str:
      for i in key:
        value += ord(i)
    index = (value*3)%self.size
    return index


  def add(self,key,value):
    index = self.hash(key)
    if not self._buckets[index]: self._buckets[index] = LinkedList()
    self._buckets[index].append([key,value])


  def get(self,key):
    index = self.hash(key)
    if self._buckets[index]:
      linked_list = self._buckets[index]
      current = linked_list.head
      while current:
        if current.value[0] == key:
          return current.value[1]
        current = current.next


  def contains(self,key):
    index = self.hash(key)

    if self._buckets[index]:
      linked_list = self._buckets[index]
      current = linked_list.head
      while current:
        if current.value[0] == key:
          return True
        current = current.next
      # return self._buckets[index].includes(key)
    return False


# CC31
def repeated_word(string):
  hash_table = HashTable()
  string = string.replace(',',' ').replace('.',' ').split(' ')
  for i in string:
    i = i.lower()
    if i and hash_table.contains(i): return(i)
    hash_table.add(i,i)


# CC32
def tree_intersection(tree1,tree2):
  tree1_list = tree1.pre_order()
  tree2_list = tree2.pre_order()
  hash_table = HashTable()
  result = []
  for i in tree1_list:
    hash_table.add(i,i)
  for i in tree2_list:
    if hash_table.contains(i):
      result.append(i)
  return result


# CC34
def biggest_repeat(string):
  hash_table = HashTable()
  string = string.replace(',',' ').replace('.',' ').replace(':',' ').split(' ')
  print(string)

  biggest_value = 0
  biggest_key = ''

  for i in string:
    i = i.lower()
    if i and hash_table.contains(i):
      value = hash_table.get(i)
      value+=1
      index = hash_table.hash(i)
      hash_table._buckets[index].head = Node([i,value])
      if value > biggest_value:
        biggest_value = value
        biggest_key = i
    elif i:
      value=1
      hash_table.add(i,value)

  return biggest_key



if __name__ =='__main__':
# CC30
  hash_table = HashTable()
  hash_table.add('yahia','24')
  hash_table.add('yaiha','30')
  hash_table.add('person','age')
  # print(hash_table.get('yahia'))
  # print(hash_table.get('yaiha'))
  # print(hash_table.get('person'))
  # print(hash_table.get('not'))
  # print(hash_table.contains('yahia'))
  # print(hash_table.contains('yaiha'))
  # print(hash_table.contains('test'))
  # print(hash_table.hash('8000'))

# CC31
  # print(repeated_word("Once upon a time, there was was was was was a brave princess who... who who"))
  # print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
  # print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))

# CC32
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

  # print(tree_intersection(binary_tree1,binary_tree2))

  print(biggest_repeat("Once upon a time, there was was was was was a brave princess who... who who"))
