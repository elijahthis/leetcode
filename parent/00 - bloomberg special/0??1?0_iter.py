from collections import deque

def generate_all_iterative(s: str):
    """
    Question: Given a string like "01?0". 
    # If ? can be 0 or 1,  print all possible outcomes
    """
    # No recursion → avoids recursion depth limits.
    # Straightforward logic → uses simple list transformations.

    res = deque([""])  # start with one empty string
    
    for ch in s:
        if ch == "?":
            # For each current string, branch it into two:
            # one with '0' and one with '1'
            res = deque([curr + bit for curr in res for bit in "01"])
        else:
            # If the character is not '?', just append it to each existing string
            res = deque([curr + ch for curr in res])
    
    return list(res)
