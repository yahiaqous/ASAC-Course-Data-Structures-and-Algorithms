class Node:
  def __init__(self,value=""):
    self.value=value
    self.next = None
  def __str__(self):
    return str(self.value)


class LinkedList():
  def __init__(self):
    self.head = None

  def __str__(self):
    current = self.head
    string = ''

    while current:
      string+=str(current)+' -> '
      current=current.next
    string+="None"
    return string

  def insert(self, value):
    node = Node(value)
    if self.head:
      node.next=self.head
    self.head = node

  def includes(self,value):
    current = self.head
    while current:
      # if value ==current.value[0]:
      if current.value == value:
          return True
      current = current.next
    return False

  def append(self,new_value):
    node = Node(new_value)
    current=self.head
    if current:
      while current.next:
        current = current.next
      current.next = node
    else:
      self.head = node
