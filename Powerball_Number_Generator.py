import random
import time

ballCount = 0
chosenNumbers = []
countPrint = 0

while len(chosenNumbers) <= 5:
    randNum = random.randint(1, 69)
    if randNum not in chosenNumbers:
        chosenNumbers.append(randNum)

chosenNumbers[5] = random.randint(1, 26)

for countPrint in chosenNumbers:
    print(countPrint, end = " ")
    time.sleep(3)
    countPrint += 1
