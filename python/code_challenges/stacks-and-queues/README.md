# Challenge Summary

Create a new class called pseudo queue.

- Do not use an existing Queue.

- Instead, this PseudoQueue class will implement our standard queue interface

- Internally, utilize 2 Stack instances to create and manage the queue

## Whiteboard Process

![CC11 Whiteboard](pictures/CC11.jpg)

## Solution

Try this code:

    if **name**=="**main**":

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
