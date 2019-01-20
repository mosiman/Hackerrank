#!/bin/python3

n = int(input())

clouds = list(map(int, input().split(' ')))

# Q: will greedy always minimize?
# i.e., always jump 2. If blockage, jump 1.
# Proof?: 

currPos = 0
numMoves = 0

while currPos < n-1:
    if clouds[currPos+2] != 1:
        currPos += 2
    else:
        currPos += 1
    numMoves += 1

print(numMoves)


