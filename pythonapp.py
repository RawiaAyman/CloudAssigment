import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data (you can run this once outside the script)
nltk.download('stopwords')
nltk.download('punkt')

# File path
file_path = "paragraphs.txt"

# Read text from file
with open(file_path, 'r') as file:
    text = file.read()

# Set of English stopwords
stop_words = set(stopwords.words('english'))

# Tokenize words
word_tokens = word_tokenize(text)

# Filter out stopwords
filtered_words = [word for word in word_tokens if word.lower() not in stop_words]

# Function to count word frequencies
def count_word_frequencies(words):
    return Counter(words)

# Function to display word frequencies
def display_word_frequencies(word_freq):
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

# Count word frequencies
word_freq = count_word_frequencies(filtered_words)

# Display word frequencies
display_word_frequencies(word_freq)
