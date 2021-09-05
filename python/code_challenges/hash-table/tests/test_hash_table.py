from hash_table.hash_table import HashTable, repeated_word

def test_adding_a_key_and_value_to_hashtable():
  hash_table = HashTable()
  hash_table.add('yahia','24')
  assert hash_table.get('yahia') == '24'

def test_retrieving_based_on_a_key_returns_the_value_stored():
  hash_table = HashTable()
  hash_table.add('yahia','24')
  assert hash_table.get('yahia') == '24'

def test_returns_null_for_a_key_that_does_not_exist_in_the_hashtable():
  hash_table = HashTable()
  assert hash_table.get('test') == None

def test_handle_a_collision_within_the_hashtable():
  hash_table = HashTable()
  hash_table.add('yahia','24')
  hash_table.add('yaiha','30')
  print(hash_table.contains('yahia'))
  print(hash_table.contains('yaiha'))

def test_retrieve_a_value_from_a_bucket_within_the_hashtable_that_has_a_collision():
  hash_table = HashTable()
  hash_table.add('yahia','24')
  hash_table.add('yaiha','30')
  assert hash_table.get('yahia') == '24'
  assert hash_table.get('yaiha') == '30'

def test_hash_a_key_to_an_in_range_value():
  hash_table = HashTable()
  assert hash_table.hash('8000')< hash_table.size

def test_repeated_word():
  assert repeated_word("Once upon a time, there was a brave princess who...") == 'a'
  assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == 'it'
  assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == 'summer'
