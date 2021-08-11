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


# CC12
class Cat():
  def __init__(self, name="",next=None):
      self.name = name
      self.next = next
      self.type='cat'

  def __str__(self):
        return str(self.name)

class Dog():
  def __init__(self, name="",next=None):
      self.name = name
      self.next = next
      self.type='dog'

  def __str__(self):
        return str(self.name)

class AnimalShelter():
  def __init__(self, animal = None):
      self.front = animal
      self.rear = animal

  def __str__(self):
        current = self.front
        string = ''

        while current:
            string+=str(current)+' -> '
            current=current.next
        string+="None"
        return string

  def enqueue(self,name,type):
    if type == 'cat':
      node = Cat(name)
      self.rear.next = node
      self.rear = node
    elif type == 'dog':
      node = Dog(name)
      self.rear.next = node
      self.rear = node

  def dequeue(self, pref):
    if pref == 'dog':
      current = self.front
      prev = current
      while current.type != 'dog':
        prev = current
        current=current.next

      if prev != self.front:
        prev.next = current.next
        current.next=None
      else:
        prev=prev.next
        current.next = None
        self.front=prev
      return current.name

    elif pref == 'cat':
      current = self.front
      prev = current
      while current.type != 'cat':
        prev = current
        current=current.next

      if prev != self.front:
        prev.next = current.next
        current.next=None
      else:
        prev=prev.next
        current.next = None
        self.front=prev
      return current.name

    else:
      return 'null'

  def peek(self):
    if self.peek:
      return (self.front.name)
    else:
      raise Exception('Animal Shelter is Empty')


# CC13
def validate_brackets(string):

  starting_symbols = ["[","{","("]
  ending_symbols = ["]","}",")"]
  check_list = []

  for i in string:
    if i in starting_symbols:
      check_list.append(i)

    elif i in ending_symbols:
      index = ending_symbols.index(i)

      if ((len(check_list) > 0) and (starting_symbols[index] == check_list[len(check_list)-1])):
        check_list.pop()
      else:
        return False

  if len(check_list) == 0:
    return True
  else:
    return False



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
  # print(psuedo_queue)
  psuedo_queue.enqueue(5)
  psuedo_queue.enqueue(5)
  # print(psuedo_queue)
  # print(psuedo_queue.dequeue())
  # print(psuedo_queue)
  # print(psuedo_queue.dequeue())
  # print(psuedo_queue)

# CC12
  animal1 = Cat('cat1')
  animal2 = Cat('cat2')
  animal3 = Dog('dog1')
  animal4 = Dog('dog2')
  animal_shelter=AnimalShelter()
  animal_shelter.front=animal1
  animal_shelter.rear=animal4
  animal1.next=animal2
  animal2.next=animal3
  animal3.next=animal4
  # print(animal_shelter)
  animal_shelter.enqueue('dog3','dog')
  # print(animal_shelter)
  # print(animal_shelter.dequeue('cat'))
  # print(animal_shelter)

# CC13
  print(validate_brackets('[({}]'))
  print(validate_brackets('()[[Extra Characters]]'))
