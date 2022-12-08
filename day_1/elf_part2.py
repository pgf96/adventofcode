import numpy as np

data = []
with open('d1_input.txt') as f:
    line = []
    for lines in f:
        if (lines.strip() == ""):
            data.append(line)
            line = []
            continue
        line.append(int(lines.strip()))
if (line):
    data.append(line)

elfCalorieTotal = []
for elf in (data):
    elfCalorieTotal.append(np.sum(elf))

maxCalorie = -1
for idx, elfCalorie in enumerate(elfCalorieTotal):
    if elfCalorie > maxCalorie:
        maxCalorie = elfCalorie
        max = (idx, maxCalorie)

elfCalorieTotal.sort(reverse=True)

total = 0
for x in range(3):
    print(elfCalorieTotal[x])
    total += elfCalorieTotal[x]
print(total)
