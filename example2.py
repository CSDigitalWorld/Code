import string
from collections import Counter

# Sample text (in practice, this would be loaded from multiple files)
text = """
Intellectual property law is a legal field that protects the rights of creators of original works.
Lawyers specializing in this area deal with issues such as copyright infringement, patent disputes,
and trademark violations. Understanding the common terminology used in these cases is crucial for
preparing legal arguments and strategies.
"""
# Display the raw text to understand its structure
print("Raw text:\n", text)

# Preprocess the text
def preprocess_text(text):
   # Convert to lowercase
   text = text.lower()
   # Remove punctuation
   text = text.translate(str.maketrans('', '', string.punctuation))
   return text
# Display preprocessed text
preprocessed_text = preprocess_text(text)
print("Preprocessed text:\n", preprocessed_text)

# Split the text into words
words = preprocessed_text.split()
print("Words list:\n", words)

# Define common stopwords
stopwords = set(["the", "and", "is", "in", "for", "of", "with", "a", "to", "as", "on", "this"])
# Remove stopwords from the list of words
filtered_words = [word for word in words if word not in stopwords]
print("Filtered words list:\n", filtered_words)

# Function to count word frequencies
def count_word_frequencies(words):
   return Counter(words)

# Get word frequencies
word_counts = count_word_frequencies(filtered_words)
print("Word frequencies:\n", word_counts)
# Function to get the top N most common words
def get_top_words(word_counts, N=10):
   return word_counts.most_common(N)

# Get the top 10 most common words
top_words = get_top_words(word_counts)
print("Top 10 most common words:")
for word, count in top_words:
   print(f"{word}: {count}")

# the most_common method is part of the Counter module

# Test with different sample texts
test_texts = [
   "Intellectual property rights and laws.",
   "Copyright and trademark issues in legal cases.",
   "Patent disputes are common in intellectual property law."
]

# Function to analyze text
def analyze_text(text):
   preprocessed_text = preprocess_text(text)
   words = preprocessed_text.split()
   filtered_words = [word for word in words if word not in stopwords]
   word_counts = count_word_frequencies(filtered_words)
   top_words = get_top_words(word_counts)
   return top_words

# Run tests
for i, test_text in enumerate(test_texts):
   print(f"\nTest {i+1} results:")
   print(analyze_text(test_text))
