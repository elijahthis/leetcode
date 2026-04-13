import random, os

def count_lines_in_file(filepath):
    try:
        contents = os.listdir(filepath)
        return contents
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

questions = count_lines_in_file("/Users/elijahoyerinde/Documents/leetcode/parent")
count = len(questions)

if count > 0:
    sample_size = min(5, count)
    print(count)
    for i in random.sample(range(count), sample_size):
        print(questions[i].strip())
