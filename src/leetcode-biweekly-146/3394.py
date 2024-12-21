from collections import defaultdict
from typing import List


class Solution:
    def checkValidCuts(self, n: int, r: List[List[int]]) -> bool:
        n = len(r)
        y, x = [], []
        for i, (sx, sy, ex, ey) in enumerate(r):
            y.append((sy, 1, i))
            y.append((ey, 0, i))

            x.append((sx, 1, i))
            x.append((ex, 0, i))

        y.sort()
        x.sort()
        processed, left = 0, n
        processing = 0
        cnt = 0
        for pt, type, idx in y:
            if type == 0:
                processed += 1
                processing -= 1
                left -= 1
            elif type == 1:
                processing += 1
            if processing == 0 and processed > 0 and left > 0:
                cnt += 1

        if cnt >= 2:
            return True

        processed, left = 0, n
        processing = 0
        cnt = 0

        for pt, type, idx in x:
            if type == 0:
                processed += 1
                processing -= 1
                left -= 1
            elif type == 1:
                processing += 1
            if processing == 0 and processed > 0 and left > 0:
                cnt += 1

        return cnt >= 2
