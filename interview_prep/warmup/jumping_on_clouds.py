#!/bin/python3

n = int(input())

clouds = list(map(int, input().rstrip().split(' ')))

# Q: will greedy always minimize?
# i.e., always jump 2. If blockage, jump 1.
# Proof?: 

currPos = 0
numMoves = 0

while currPos <= n-2:
    try:
        if clouds[currPos+2] != 1:
            currPos += 2
        else:
            currPos += 1
    except:
        currPos += 1

    numMoves += 1

print(numMoves)


