class sorting:

  def __init__(self) -> None:
      pass

  def merge_sort(self, A:list) -> list:
    self.merge_sort2(A, 0, len(A)-1)
    return A

  def merge_sort2(self, A, first, last):
    if first < last:
      middle = (first + last) // 2
      self.merge_sort2(A, first, middle)
      self.merge_sort2(A, middle+1, last)
      self.merge_final(A, first, middle, last)

  def merge_final(self, A, first, middle, last):
    L = A[:middle+1]
    R = A[middle+1:]
    i = j = k = 0
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        A[k] = L[i]
        i+=1
      else:
        A[k] = R[j]
        j += 1
      k += 1

a=[4,5,3,7,1,9]
srt=sorting()
print(srt.merge_sort(a))

