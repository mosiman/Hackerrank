

n = int(input())
topo = input()

currAltitude = 0
numValleys = 0
currentlyInValley = False

for step in topo:
    if step == "U":
        currAltitude += 1
    else:
        currAltitude -= 1

    if currAltitude < 0 and not currentlyInValley:
        currentlyInValley = True
        numValleys += 1
    if currAltitude >= 0 and currentlyInValley:
        currentlyInValley = False

print(numValleys)
