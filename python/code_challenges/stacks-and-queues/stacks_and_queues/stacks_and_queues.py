class Node():
  def __init__(self, value="",next=None):
      self.value = value
      self.next = next

  def __str__(self):
        return str(self.value)

class StackEmptyException(Exception):
	pass

# CC10
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


# CC11
class PseudoQueue():
  def __init__(self, node = None):
      self.front = node
      self.rear = node
      self.stack1=Stack()
      self.stack2=Stack()

  def __str__(self):
      current = self.front
      string = ''

      while current:
          string+=str(current)+' -> '
          current=current.next
      string+="None"
      return string

  def enqueue(self,value):
    self.stack1.push(value)
    self.stack1.top.next = self.front
    self.front = self.stack1.top

  def dequeue(self):
    current = self.front
    while current.next != self.rear:
      current = current.next

    self.stack1.push(current.next)
    output = self.stack1.pop()
    self.rear=current
    self.rear.next=None
    return output

  def peek(self):
    if self.peek:
      return (self.front.value)
    else:
      raise Exception('Queue is Empty')

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
  # print(stack)
  stack.push(6)
  # print(stack)
  stack.pop()
  stack.pop()
  # print(stack)
  # print(stack.peek())
  # print(stack.is_empty())

  queue=Queue()
  queue.front=node1
  queue.rear=node4
  node1.next=node2
  node2.next=node3
  node3.next=node4
  # print(queue)
  queue.enqueue(9)
  # print(queue)
  queue.dequeue()
  queue.dequeue()
  # print(queue)
  # print(queue.peek())
  # print(queue.is_empty())

# CC11
  psuedo_queue = PseudoQueue()
  psuedo_queue.front=node1
  psuedo_queue.rear=node4
  node1.next=node2
  node2.next=node3
  node3.next=node4
  print(psuedo_queue)
  psuedo_queue.enqueue(5)
  psuedo_queue.enqueue(5)
  print(psuedo_queue)
  print(psuedo_queue.dequeue())
  print(psuedo_queue)
  print(psuedo_queue.dequeue())
  print(psuedo_queue)
