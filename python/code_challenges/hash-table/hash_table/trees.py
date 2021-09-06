class Node():
  def __init__(self,value='',left=None,right=None):
      self.value = value
      self.left = left
      self.right = right
      self.next = None

  def __str__(self):
      return str(self.value)

class BinaryTree():
  def __init__(self, node=None):
      self.root = node

  def pre_order(self):
    pre_order_output = []

    def walk(root):
      pre_order_output.append(root.value)
      if (root.left): walk(root.left)
      if (root.right): walk(root.right)

    walk(self.root)
    return pre_order_output

