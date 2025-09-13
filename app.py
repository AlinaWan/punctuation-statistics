import sys
import unicodedata
from collections import Counter

# Ensure a file argument is provided
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <filename>")
    sys.exit(1)

file_path = sys.argv[1]

# Function to check if a character is punctuation
def is_punctuation(char):
    # Unicode categories starting with 'P' are punctuation
    return unicodedata.category(char).startswith('P')

# Read the file
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Filter all punctuation characters
punctuations = [c for c in text if is_punctuation(c)]

# Print all punctuation in order
print("All punctuation in order:")
print("".join(punctuations))

# Count occurrences of each punctuation
punct_count = Counter(punctuations)
total_puncts = sum(punct_count.values())

# Sort punctuations by frequency (most frequent first)
sorted_puncts = punct_count.most_common()

# Print counts with frequency percentages
print("\nCounts and frequency of each punctuation (most frequent first):")
for punct, count in sorted_puncts:
    percentage = (count / total_puncts) * 100
    print(f"{repr(punct)}: {count} ({percentage:.2f}%)")
