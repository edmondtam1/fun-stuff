import numpy as np


def create_grid(grid_string):
    rows = grid_string.strip().split("\n")
    return np.array([list(row.split()) for row in rows])


def search_word(grid, word):
    height, width = grid.shape
    word = word.upper()

    for y in range(height):
        for x in range(width):
            for dx, dy in [
                (0, 1),
                (1, 0),
                (1, 1),
                (1, -1),
                (-1, 1),
                (-1, 0),
                (0, -1),
                (-1, -1),
            ]:
                if word_fits(grid, word, x, y, dx, dy):
                    return [(x + i * dx, y + i * dy) for i in range(len(word))]
    return None


def word_fits(grid, word, x, y, dx, dy):
    height, width = grid.shape
    if not (0 <= x < width and 0 <= y < height):
        return False
    for letter in word:
        if not (0 <= x < width and 0 <= y < height) or grid[y, x] != letter:
            return False
        x += dx
        y += dy
    return True


# Define the grid
grid_string = """
T I A R R E A E R E R T R E T A R E E I T
A T E R R E I E R R T I I E R R T I E E E
R E I E T E R R A R A I E R R A A R I A R
I A E A I I I T I I R A R R T E E R A I E
I I E A R R A R A A E R R A A I R R A T T
T T A R E T R E A A T I E R R I A A R R R
E A E R I I R R I T I T E R R R T R R A I
E R I T I R R E E R E I R E E A E T T T I
R A E T A R E T I E R E I T E R A T I A E
I E I I E I E E T T E E R R T T E E E A R
I E A A R T R T I R T E T E I I A R T I R
E T R R A A T I I R I E I R R E T R I R A
R E R E T T I T E R R T E I E E I A E T I
I E A A A E E R T A E E E E A R R E A A A
E E R E E R A R A I R T T R R A A I I T R
R R T R I T E I R R E R R R I I R R I A E
E A I E E A R R E I R R E T A T E I E E T
E E I E I I E T A R A E A R I T T A T R R
I R E R E T E E T I A R T I A R T A T R A
T E T R R T I R A E I E E A I I E R R E E
"""

words_to_find = [
    "arrear",
    "rarer",
    "rearer",
    "airier",
    "eerie",
    "reiterate",
    "irritate",
    "terraria",
    "attire",
    "retreat",
    "aerate",
    "errata",
    "tiara",
    "trait",
    "retiree",
    "terrier",
]

# Create the grid
grid = create_grid(grid_string)

# Search for each word
for word in words_to_find:
    result = search_word(grid, word)
    if result:
        print(f"Found '{word}' at coordinates: {result}")
    else:
        print(f"Could not find '{word}'")
