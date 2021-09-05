from hash_table.hash_table import HashTable

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
