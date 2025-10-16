import random

def count_lines_in_file(filepath):
    try:
        with open(filepath, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

count = count_lines_in_file("/Users/elijahoyerinde/Documents/leetcode/parent/meta.txt")

print(random.sample(range(1,count), 5))