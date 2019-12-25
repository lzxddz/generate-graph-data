import os

enlish_words = []

word_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "google-10000-english.txt")

with open(word_path, 'r') as f:
    english_words = f.read().splitlines()
