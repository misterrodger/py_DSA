def contains_duplicate(arr: list[int]):
  num_set: set[int] = set()

  for num in arr:
    if num in num_set:
      return True
    num_set.add(num)

  return False

# V2
def contains_duplicate2(arr: list[int]):
  return len(arr) != len(set(arr))

print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
print(contains_duplicate([1,2,3]))