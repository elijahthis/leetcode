import random

def count_lines_in_file(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            return [line_count, lines]
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return [0, []]
    except Exception as e:
        print(f"An error occurred: {e}")
        return [0, []]

count, lines = count_lines_in_file("/Users/elijahoyerinde/Documents/leetcode/parent/meta.txt")

if count > 0:
    sample_size = min(5, count)
    for i in random.sample(range(count), sample_size):
        print(lines[i].strip())
