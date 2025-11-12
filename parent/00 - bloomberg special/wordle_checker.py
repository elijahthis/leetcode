def wordle_checker(word: str, target: str) -> str:
    """
    Implement a Wordle checker function: 
    given a word and a target, output a string that indicates which letters are correct and in the right position, 
    which are correct but in the wrong position, 
    and which are completely wrong.

    ✅ Rules Recap:
        Green (🟩) → correct letter in the correct position
        Yellow (🟨) → correct letter but wrong position
        Gray (⬜) → letter not in the target word
    """
    # O(n) — linear in word length (n ≤ 5 for Wordle)
    # O(1) space (since the alphabet is constant-sized)

    result = ['⬜'] * len(word)
    target_count = {}

    # Count letters in target for later yellow checks
    for ch in target:
        target_count[ch] = target_count.get(ch, 0) + 1

    # First pass: mark greens
    for i in range(len(word)):
        if word[i] == target[i]:
            result[i] = '🟩'
            target_count[word[i]] -= 1

    # Second pass: mark yellows
    for i in range(len(word)):
        if result[i] == '⬜' and word[i] in target_count and target_count[word[i]] > 0:
            result[i] = '🟨'
            target_count[word[i]] -= 1

    return ''.join(result)
