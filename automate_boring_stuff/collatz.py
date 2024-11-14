def collatz(N):
    #The while loop will take input from the out of the math within the loop until the output is 1.
    while N != 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = 3 * N + 1
        print(N)

#test and call function
N = int(input())
collatz(N)
