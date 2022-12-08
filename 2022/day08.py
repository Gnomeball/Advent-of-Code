with open("data/day08.txt") as file:
    trees = [ list(map(int, tree)) for tree in file.read().splitlines() ]
    v_trees = list(zip(*trees))

HEIGHT = len(trees)
WIDTH = len(v_trees)

def visible(x, y, trees):
    if x == 0 or y == 0: return True
    left = list(reversed(trees[y][:x+1]))
    right = trees[y][x:]
    return ( left[0]  == max(left)  and  left.count(left[0])  == 1
      ) or ( right[0] == max(right) and right.count(right[0]) == 1 )

can_be_seen = 2 * (HEIGHT -1) + 2 * (WIDTH -1) + [
        visible(x, y, trees) or visible(y, x, v_trees)
            for x in range(1, WIDTH -1)
            for y in range(1, HEIGHT -1)
    ].count(True)

print(f"Part one = {can_be_seen}")

tree_scores = [ [ 1 for _ in range(WIDTH) ] for _ in range(HEIGHT) ]

def score_tree(x, y):
    for i in range(x + 1, WIDTH):
        if trees[y][i] >= trees[y][x]:
            break
    return i - x

for i in range(4):
    for y in range(1, HEIGHT -1):
        for x in range(1, WIDTH -1):
            tree_scores[y][x] *= score_tree(x, y)
    trees = list(zip(*trees))[::-1]
    tree_scores = list([*i] for i in zip(*tree_scores))[::-1]

treehouse_score = max(score for tree in tree_scores for score in tree)

print(f"Part two = {treehouse_score}")
