#40 TOP ALGORITMOS | QUICK SORT
"""
 * Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort", creado por C.A.R. Hoare.
 * - Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
 *   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
 * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos los más famosos de la historia.
https://llego.dev/posts/quick-sort-python/
"""


def partition(arr, low, high):
  """make the partition of the array"""
  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i + 1

def quickSort(arr, low, high):
  """sort the array"""
  if low < high:
    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)


arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, len(arr)-1)

print(arr)