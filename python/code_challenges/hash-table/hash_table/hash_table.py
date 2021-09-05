from linked_list import LinkedList

class HashTable():
  def __init__(self,size=1024):
      self.size = size
      self._buckets = [None] * size

# CC30
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


# CC31
def repeated_word(string):
  hash_table = HashTable()
  string = string.replace(',',' ').replace('.',' ').split(' ')
  for i in string:
    i = i.lower()
    if i and hash_table.contains(i): return(i)
    hash_table.add(i,i)




if __name__ =='__main__':
# CC30
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

# CC31
  print(repeated_word("Once upon a time, there was a brave princess who..."))
  print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
  print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
