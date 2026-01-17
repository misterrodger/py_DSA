from collections import Counter

def is_anagram(input1: str, input2: str):
  return sorted(input1) == sorted(input2)

def is_anagram2(input1: str, input2: str):
  if len(input1) != len(input2):
    return False
  
  result = input2

  for letter in input1:
    result = result.replace(letter, '', 1)

  return len(result) == 0

def is_anagram3(input1: str, input2: str):
  counter = Counter(input1)
  counter2 = Counter(input2)

  return counter == counter2


print(is_anagram3('anagram', 'nagaram'))
print(is_anagram3('anagram', 'fail'))
