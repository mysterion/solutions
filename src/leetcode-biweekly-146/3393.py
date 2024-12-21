from collections import defaultdict

m = 10**9 + 7


class Solution:
    def countPathsWithXorValue(self, g: List[List[int]], k: int) -> int:
        h, w = len(g), len(g[0])
        x = [[defaultdict(int) for _ in range(w)] for _ in range(h)]
        x[0][0][g[0][0]] = 1
        for i in range(h):
            for j in range(w):
                if i + 1 < h:
                    for cur, v in x[i][j].items():
                        x[i + 1][j][cur ^ g[i + 1][j]] = (x[i + 1][j][cur ^ g[i + 1][j]] + v) % m
                if j + 1 < w:
                    for cur, v in x[i][j].items():
                        x[i][j + 1][cur ^ g[i][j + 1]] = (x[i][j + 1][cur ^ g[i][j + 1]] + v) % m
        return x[h - 1][w - 1][k]
