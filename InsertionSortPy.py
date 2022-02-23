import random

class sorting:

    def __init__(self) -> None:
        pass

    def insertionSort_asce(self, A:list) -> list:
        for i in range(1, len(A)):
            currNum=A[i]
            for j in range(i-1, -1, -1):
                if A[j] > currNum:
                    A[j+1] = A[j]
                    if j==0:
                        A[j] = currNum
                else:
                    A[j+1] = currNum
                    break
        return A

    def insertionSort_desc(self, A:list) -> list:
        for i in range(1, len(A)):
            currNum=A[i]
            for j in range(i-1, -1, -1):
                if A[j] < currNum:
                    A[j+1] = A[j]
                    if j==0:
                        A[j] = currNum
                else:
                    A[j+1] = currNum
                    break
        return A


srt=sorting()
a=[]
for x in range(0, 15):
    a.append(random.randint(0, 100))
print(srt.insertionSort_asce(a))
print(srt.insertionSort_desc(a))

b=list(input('Insert list of numbers: '))
print(srt.insertionSort_asce(b))
print(srt.insertionSort_desc(b))


