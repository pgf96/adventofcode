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
print(data)
for elf in (data):
    elfCalorieTotal.append(np.sum(elf))
print(elfCalorieTotal)

maxCalorie = -1
for idx, elfCalorie in enumerate(elfCalorieTotal):
    if elfCalorie > maxCalorie:
        maxCalorie = elfCalorie
        max = (idx, maxCalorie)
print(max)
