# Punctuation Stats

**Punctuation Stats** is a Python command-line tool that extracts and analyzes all punctuation from a text file.  
It prints every punctuation mark in the order they appear, and then shows a frequency table (counts + percentages), sorted by most frequent first.  

This project was inspired by [just-the-punctuation](https://just-the-punctuation.vercel.app), a neat web tool for visualizing punctuation.  
However, that tool sometimes outputs more punctuation than your text actually contains — so I made my own, ensuring accurate results with no extra characters.

---

## Features

- Reads any text file and extracts **all Unicode punctuation**, not just ASCII.  
- Prints punctuation marks in the exact order they appear.  
- Counts occurrences of each punctuation mark.  
- Calculates and displays frequency percentages.  
- Sorts results by most frequent punctuation first.  

---

## Installation

Clone this repository (or just grab the script file):

```bash
git clone https://github.com/AlinaWan/punctuation-stats.git
cd punctuation-stats
```

---

## Usage

```pwsh
python app.py <file>
```
