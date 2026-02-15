class Solution:
    def checkEqual(self, a, b) -> bool:
        c=sorted(a)
        d=sorted(b)
        return c==d