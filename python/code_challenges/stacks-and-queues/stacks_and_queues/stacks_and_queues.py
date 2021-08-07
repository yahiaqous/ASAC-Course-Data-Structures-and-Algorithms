class Node():
  def __init__(self, value="",next=None):
      self.value = value
      self.next = next

  def __str__(self):
        return str(self.value)

class StackEmptyException(Exception):
	pass

class Stack():
  def __init__(self, node = None):
      self.top = node

  def __str__(self):
        current = self.top
        string = ''

        while current:
            string+=str(current)+' -> '
            current=current.next
        string+="None"
        return string

# CC10
  def push(self,value):
    node = Node(value)
    node.next = self.top
    self.top = node

  def pop(self):
    if self.top:
      current = self.top
      self.top = current.next
      current.next=None
      return current.value
    else:
      raise Exception('Stack is Empty')

  def peek(self):
    if self.top:
      return (self.top.value)
    else:
      raise Exception('Stack is Empty')

  def is_empty(self):
    return (self.top == None)




class Queue():
  def __init__(self, node = None):
      self.front = node
      self.rear = node

  def __str__(self):
        current = self.front
        string = ''

        while current:
            string+=str(current)+' -> '
            current=current.next
        string+="None"
        return string

# CC10
  def enqueue(self,value):
    node = Node(value)
    node.next = self.front
    self.front = node

  def dequeue(self):
    if self.peek:
      current = self.front
      self.front = current.next
      current.next=None
      return current.value
    else:
      raise Exception('Queue is Empty')


  def peek(self):
    if self.peek:
      return (self.front.value)
    else:
      raise Exception('Queue is Empty')

  def is_empty(self):
    return (self.front == None or self.rear == None)



if __name__=="__main__":

# CC10
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  node4 = Node(4)
  stack=Stack()
  stack.top=node1
  node1.next=node2
  node2.next=node3
  node3.next=node4
  print(stack)
  stack.push(6)
  print(stack)
  stack.pop()
  stack.pop()
  print(stack)
  print(stack.peek())
  print(stack.is_empty())


# CC10
  queue=Queue()
  queue.front=node1
  queue.rear=node4
  node1.next=node2
  node2.next=node3
  node3.next=node4
  print(queue)
  queue.enqueue(9)
  print(queue)
  queue.dequeue()
  queue.dequeue()
  print(queue)
  print(queue.peek())
  print(queue.is_empty())

