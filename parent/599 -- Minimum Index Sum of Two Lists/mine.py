class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashM = {}
        total = float("inf")
        res = []

        for idx, word in enumerate(list1):
            hashM[word] = idx
        
        for idx, word in enumerate(list2):
            if word in hashM:
                if (hashM[word] + idx) < total:
                    total = hashM[word] + idx
                    res = [word]
                elif (hashM[word] + idx) == total:
                    res.append(word)
        
        return res
