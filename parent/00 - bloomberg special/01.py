def generateString(s: str) -> str:
    # 0100?0??1
    res = []

    def backtrack(i: int, currStr: List[str]):
        if i == len(s):
            str.append("".join(currStr))
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