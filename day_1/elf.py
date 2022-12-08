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


lowElfCalorie = -1
maxCalorie = (-1, lowElfCalorie)
for idx, elfCalorie in enumerate(elfCalorieTotal):
    if elfCalorie > maxCalorie[lowElfCalorie]:
        maxCalorie = (idx, elfCalorie)

print(maxCalorie)

