"""
Из моего интервью на стажировку. Весна 2023

input: [1, 3, 5, 7, 8, 8, 9, 11, 12, 13, 20]
output: 1,3,5,7-9,11-13,20
"""

def way1(array: list) -> str:
  """Решение похоже на слияение интервалов(leetcode: merge intervals)"""
  array.sort()
  
  ans = []
  for x in array:
      if not ans:
          ans.append([x, x])
      else:
          if ans[-1][1] == x or ans[-1][1] + 1== x:
              ans[-1][1] = x
          else:
              ans.append([x, x])
  return ','.join(f'{x[0]}-{x[1]}' if x[0] != x[1] else str(x[0]) for x in ans)

def way2(array: list) -> str:
  """Решение через два указателя"""
  array.sort()
  
  l = 0
  r = 0
  array.append(float('inf')) # Добавляем элемент, которого точно нет в массиве, чтобы обработать конец массива
  while r < len(array) - 1:
      if array[r] == array[r+1] or array[r] + 1 == array[r + 1]:
          r += 1
      else:
          if l == r:
              ans.append(str(array[r]))
          else:
              ans.append(f'{array[l]}-{array[r]}')
              l = r
          r += 1
          l += 1
  return ','.join(ans)
          
