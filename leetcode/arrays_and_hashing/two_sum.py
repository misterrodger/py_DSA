def two_sum2(input_list: list[int], target: int):
  for i, x in enumerate(input_list):
    for j, y in enumerate(input_list[i + 1:]):
      if x + y == target:
        return [i, j + 1]

print(two_sum2([2, 11, 7, 15], 9))