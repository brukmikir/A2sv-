class Solution:
    def isSubset(self, a, b):
        from collections import Counter
        
        freqA = Counter(a)
        freqB = Counter(b)
        
        for key in freqB:
            if freqB[key] > freqA.get(key, 0):
                return False
        return True

    