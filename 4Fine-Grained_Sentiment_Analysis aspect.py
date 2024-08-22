import pandas as pd
import re
from collections import defaultdict
# Load the CSV file
data = pd.read_csv('output.csv')
# Simple function to extract nouns and adjectives as aspects
def simple_aspect_extraction(text_data):
    aspects = defaultdict(int)
    for text in text_data:
        # Tokenize the text
        words = re.findall(r'\b\w+\b', text.lower())
        # Extract potential aspects (nouns/adjectives)
        for word in words:
            if word.isalpha() and len(word) > 2:  # Filter out short words and non-alphabetic tokens
                aspects[word] += 1
    return aspects
# Perform aspect extraction
aspect_count_simple = simple_aspect_extraction(data['text'])
# Get the most common aspects
common_aspects_simple = sorted(aspect_count_simple.items(), key=lambda x: x[1], reverse=True)[:10]
# Display the most common aspects
print(common_aspects_simple)

