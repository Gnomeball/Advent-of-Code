ROW, COLUMN = 3010, 3019

iter = sum(range(ROW + COLUMN - 1)) + COLUMN
# Only 18.2~ million ...

CODE = 20151125

for i in range(iter - 1):
	CODE = (CODE * 252533) % 33554393

print(f"Part one = {CODE}")
