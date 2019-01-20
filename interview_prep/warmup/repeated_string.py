s = input().rstrip()
n = int(input())

# substring length l1, n is repeated length.
# numA is number times a in s
# numA*(l1//n) is lowerbound
# get the rest with numA2 = number times a in s[0: l1 mod n]


l1 = len(s)
numA = sum( map(lambda x: 1 if x == "a" else 0, s))

lowbound = numA * (n//l1)

sExtra = s[0:n%l1]

numB = sum( map(lambda x: 1 if x == "a" else 0, sExtra))

print(lowbound + numB)
