from linked_list import LinkedList

class HashTable():
  def __init__(self,size=1024):
      self.size = size
      self._buckets = [None] * size


  def hash(self,key):
    value = 0
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


if __name__ =='__main__':
  hash_table = HashTable()
  hash_table.add('yahia','24')
  hash_table.add('yaiha','30')
  hash_table.add('person','age')
  print(hash_table.get('yahia'))
  print(hash_table.get('yaiha'))
  print(hash_table.get('person'))
  print(hash_table.get('not'))
  print(hash_table.contains('yahia'))
  print(hash_table.contains('yaiha'))
  print(hash_table.contains('test'))
  print(hash_table.hash('8000'))
