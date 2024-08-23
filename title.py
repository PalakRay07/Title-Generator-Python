

import tkinter as tk
from tkinter import ttk
import nltk
from nltk.corpus import wordnet

def generate_titles(keywords):
  """Generates titles based on given keywords using simple templates and wordnet expansion.

  Args:
    keywords: A string containing the keywords.

  Returns:
    A list of generated titles.
  """

  nltk.download('wordnet')  # Download WordNet corpus if not already downloaded

  expanded_keywords = []
  for keyword in keywords.split():
    for synset in wordnet.synsets(keyword):
      for lemma in synset.lemmas():
        expanded_keywords.append(lemma.name())

  templates = [
    "{}: A Comprehensive Guide",
    "How to Master {}",
    "The Ultimate Guide to {}",
    "{} Tips and Tricks",
    "Unleash the Power of {}",
    "Transform Your Life with {}"
  ]

  titles = []
  for keyword in expanded_keywords:
    for template in templates:
      title = template.format(keyword)
      titles.append(title)
  return titles

def on_generate_click():
  keywords = entry.get()
  generated_titles = generate_titles(keywords)
  result_label.config(text="\n".join(generated_titles))

# Create the main window
root = tk.Tk()
root.title("Title Generator")

# Create input field and label
keyword_label = ttk.Label(root, text="Enter Keywords:")
keyword_label.pack()
entry = ttk.Entry(root)
entry.pack()

# Create generate button
generate_button = ttk.Button(root, text="Generate Titles", command=on_generate_click)
generate_button.pack()

# Create result label
result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
