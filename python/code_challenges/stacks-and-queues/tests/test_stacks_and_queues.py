import pytest
from stacks_and_queues.stacks_and_queues import Node, Stack,Queue,StackEmptyException,PseudoQueue

# CC10
def test_push_onto_stack():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  stack=Stack()
  stack.top=node1
  node1.next=node2
  node2.next=node3
  stack.push(4)
  assert stack.top.value == 4

def test_push_multiple_values_onto_stack():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  stack=Stack()
  stack.top=node1
  node1.next=node2
  node2.next=node3
  stack.push(5)
  assert stack.top.value == 5
  stack.push(7)
  assert stack.top.value == 7

def test_pop_off_stack():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  stack=Stack()
  stack.top=node1
  node1.next=node2
  node2.next=node3
  stack.pop()
  assert stack.top.value == 2

def test_empty_a_stack_after_multiple_pops():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  stack=Stack()
  stack.top=node1
  node1.next=node2
  node2.next=node3
  stack.pop()
  stack.pop()
  stack.pop()
  assert stack.is_empty

def test_peek_the_next_item_on_the_stack():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  stack=Stack()
  stack.top=node1
  node1.next=node2
  node2.next=node3
  assert stack.peek()==1

def test_instantiate_an_empty_stack():
  stack=Stack()
  assert stack

def test_raises_exception_on_empty_stack_pop_or_peek():
  stack=Stack()
  with pytest.raises(StackEmptyException, match ="Stack is Empty"):
    stack.pop()



def test_enqueue_into_queue():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  queue=Queue()
  queue.front=node1
  node1.next=node2
  node2.next=node3
  queue.rear=node3
  queue.enqueue(4)
  assert queue.rear.value == 4

def test_enqueue_multiple_values_into_queue():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  queue=Queue()
  queue.front=node1
  node1.next=node2
  node2.next=node3
  queue.rear=node3
  queue.enqueue(5)
  assert queue.rear.value == 5
  queue.enqueue(7)
  assert queue.rear.value == 7

def test_dequeue_out_of_queue():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  queue=Queue()
  queue.front=node1
  node1.next=node2
  node2.next=node3
  queue.dequeue()
  assert queue.front.value == 2

def test_empty_a_equeue_after_multiple_dequeues():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  queue=Queue()
  queue.front=node1
  node1.next=node2
  node2.next=node3
  queue.dequeue()
  queue.dequeue()
  queue.dequeue()
  assert queue.is_empty

def test_peek_into_queue():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  queue=Queue()
  queue.front=node1
  node1.next=node2
  node2.next=node3
  assert queue.peek()==1

def test_instantiate_an_empty_queue():
  queue=Queue()
  assert queue

def test_raises_exception_on_empty_queue_dequeue_or_peek():
  queue=Queue()
  with pytest.raises(StackEmptyException, match ="Stack is Empty"):
    queue.dequeue()


# CC11
def test_enqueue_into_pseudoqueue():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  pseudoqueue=PseudoQueue()
  pseudoqueue.top=node1
  node1.next=node2
  node2.next=node3
  pseudoqueue.enqueue(4)
  assert pseudoqueue.front.value == 4

def test_multiple_enqueue_into_pseudoqueue():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  pseudoqueue=PseudoQueue()
  pseudoqueue.top=node1
  node1.next=node2
  node2.next=node3
  pseudoqueue.enqueue(4)
  assert pseudoqueue.front.value == 4
  pseudoqueue.enqueue(6)
  assert pseudoqueue.front.value == 6

def test_dequeue_out_of_psuedoqueue():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  psuedoqueue=Queue()
  psuedoqueue.front=node1
  node1.next=node2
  node2.next=node3
  psuedoqueue.dequeue()
  assert psuedoqueue.front.value == 2

def test_empty_a_equeue_after_multiple_dequeues_psuedoqueue():
  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(3)
  psuedoqueue=Queue()
  psuedoqueue.front=node1
  node1.next=node2
  node2.next=node3
  psuedoqueue.dequeue()
  psuedoqueue.dequeue()
  psuedoqueue.dequeue()
  assert psuedoqueue.is_empty
