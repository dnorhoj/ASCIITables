import random
import string

import asciitables

data = []

ROWS = 5
COLUMNS = 3


# Create random data
for i in range(ROWS):
    data.append([])
    for j in range(COLUMNS):
        # Random text
        data[-1].append("".join([random.choice(string.ascii_letters)
                        for _ in range(random.randint(5, 10))]))


# Try all themes
for i in filter(lambda x: "THEME" in x, dir(asciitables)):
    print(f"\n{i}")
    print(asciitables.create_table(
        data,
        theme=vars(asciitables)[i],
        # header=False,
        # separated=True,
    ))
