h, w, x, y = map(int, input().split())
g = [input() for i in range(h)]
x -= 1
y -= 1
s = input()

v = set()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ds = "URDL"


def pr(p, q):
    for i in range(h):
        for j in range(w):
            if (i, j) == (p, q):
                print("X", end="")
                continue
            print(g[i][j], end="")
        print()


if g[x][y] == "@":
    v.add((x, y))


for c in s:
    i = ds.find(c)
    nx, ny = x + dx[i], y + dy[i]
    if g[nx][ny] != "#":
        if g[nx][ny] == "@":
            v.add((nx, ny))
        x, y = nx, ny
print(x + 1, y + 1, len(v))
