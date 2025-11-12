
def generate_all(s: str) -> List[str]:
    # 010?10?1
    res = []

    def backtrack(i: int, currStr: List[str]) -> None:
        if i == len(s):
            res.append("".join(currStr))
            return

        if s[i] == "?":
            for char in ["0", "1"]:
                currStr.append(char)
                backtrack(i+1, currStr)
                currStr.pop()
        else:
            currStr.append(s[i])
            backtrack(i+1, currStr)
            currStr.pop()

    backtrack(0, [])
    return res
    
        