def generate_all(s: str) -> List[str]:
    """
    Question: Given a string like "01?0". 
    # If ? can be 0 or 1,  print all possible outcomes
    """
    # 0??1?0
    # Time: O(2^k),
    # Space: O(2^k),
    
    res = []

    def backtrack(i: int, currStr):
        if len(currStr) == len(s):
            res.append("".join(currStr))
            return

        if s[i] == "?":
            for ch in ["0", "1"]:
                currStr.append(ch)
                backtrack(i+1, currStr)
                currStr.pop()
        else:
            currStr.append(s[i])
            backtrack(i+1, currStr)
            currStr.pop()

    
    backtrack(0, [])
    return res