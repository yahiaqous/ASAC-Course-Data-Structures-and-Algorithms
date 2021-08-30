from merge_sort.merge_sort import merge_sort,merge

def test_merge_sort():
  assert merge_sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]
  assert merge_sort([]) == []
