class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        l1, w1 = ax2-ax1, ay2-ay1
        l2, w2 = bx2-bx1, by2-by1

        bigArea = l1*w1 + l2*w2
        insideArea = 0

        lox, hix = max(ax1, bx1), min(ax2, bx2)
        loy, hiy = max(ay1, by1), min(ay2, by2)

        if lox < hix and loy < hiy:
            insideArea = (hix-lox) * (hiy-loy)

        return bigArea - insideArea
        