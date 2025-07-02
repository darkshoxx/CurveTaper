import os

HERE = os.path.abspath(os.path.dirname(__file__))
SCRATCH = os.path.join(HERE, "scratch.py")

with open(SCRATCH, "r") as f:
    lines = f.readlines()
to_pop = []

for index in range(len(lines)):
    if lines[index][:4] == ">>> ":
        lines[index] = lines[index][4:]
    if lines[index][:3] == ">>>":
        lines[index] = lines[index][3:]
    if lines[index][:2] == "# ":
        to_pop.append(index)

for item in reversed(to_pop):#
    lines.pop(item)

with open(SCRATCH, "w") as f:
    f.writelines(lines)