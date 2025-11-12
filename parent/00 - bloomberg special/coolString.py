from collections import Counter

def is_cool_string(s: str):
    freq = Counter(s)
    counts = list(freq.values())
    unique_counts = set(counts)

    # ✅ 1. Check if already cool
    if len(unique_counts) == 1:
        return True, True  # (is_cool, can_be_made_cool)

    # ✅ 2. Check if it can be made cool by one add/remove
    if len(unique_counts) > 2:
        return False, False

    # When there are exactly 2 unique frequencies
    min_count, max_count = min(unique_counts), max(unique_counts)

    # Case 1: One character occurs once, and others have the same count
    # Example: "aabbccd" -> remove one 'd'
    if counts.count(min_count) == 1 and min_count == 1:
        return False, True

    # Case 2: One character has one more occurrence than others
    # Example: "aabbccc" -> remove one 'c'
    if counts.count(max_count) == 1 and max_count - min_count == 1:
        return False, True

    return False, False


# ✅ Examples
print(is_cool_string("aaabbbccc"))  # (True, True)
print(is_cool_string("abcd"))       # (True, True)
print(is_cool_string("abbcd"))      # (False, True)
print(is_cool_string("aabbcccc"))   # (False, True)
print(is_cool_string("aabbccdde"))  # (False, False)
