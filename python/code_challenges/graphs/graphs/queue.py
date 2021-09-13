class Node():
  def __init__(self, value="",next=None):
      self.value = value
      self.next = next

  def __str__(self):
        return str(self.value)

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
    self.rear.next = node
    self.rear = node

  def dequeue(self):
    if self.peek:
      current = self.front
      self.front = current.next
      current.next=None
      return current.value
    else:
      raise Exception('Queue is Empty')

  def peek(self):
    if self.front:
      return (self.front.value)
    else:
      raise Exception('Queue is Empty')

  def is_empty(self):
    return (self.front == None or self.rear == None)

if __name__=="__main__":
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  node4 = Node(4)
  queue=Queue()
  queue.front=node1
  queue.rear=node4
  node1.next=node2
  node2.next=node3
  node3.next=node4
  queue.enqueue(9)
  print(queue)
  queue.dequeue()
  queue.dequeue()
  print(queue)
  print(queue.peek())
  print(queue.is_empty())
