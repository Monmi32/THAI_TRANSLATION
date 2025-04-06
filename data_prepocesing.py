import pandas as pd
import numpy as np
df = pd.read_csv('/content/translation_dataset.csv')

new_df = df.drop(columns=['translation', 'review_star', 'correct'])

import pandas as pd
import unicodedata
import html
import pythainlp

NORM_CODE = "NFKC"

# Define cleaning functions
def clean_text(lang, text):
    """Applies a series of text cleaning transformations."""
    if pd.isna(text):  # Handle NaN values
        return ""

    text = str(text).strip()  # Remove leading/trailing spaces
    text = html.unescape(text)  # Convert HTML entities to characters
    text = unicodedata.normalize(NORM_CODE, text) if NORM_CODE in ['NFC', 'NFD', 'NFKC', 'NFKD'] else text
    text = text.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'")  # Standardize quotes

    if lang == "th":
        text = pythainlp.util.normalize(text)  # Normalize Thai text

    # Replace escape characters
    mapping = {
        "\x94": "\"", "\x93": "\"", "\x91": "'", "\x92": "'", "\x96": "-"
    }
    for char, replacement in mapping.items():
        text = text.replace(char, replacement)

    return text

# Define filtering functions
def filter_blank_text(text):
    """Removes empty or whitespace-only text."""
    return text.strip() == ""

def filter_thai_text_without_thai_chars(text):
    """Filters Thai text that does not contain Thai characters."""
    thai_characters = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ"
    return not any(char in text for char in thai_characters)

# Apply cleaning functions to `new_df`
new_df["english_text"] = new_df["english_text"].apply(lambda x: clean_text("en", x))
new_df["thai_text"] = new_df["thai_text"].apply(lambda x: clean_text("th", x))

# Apply filtering (remove invalid rows)
new_df = new_df[~new_df["english_text"].apply(filter_blank_text)]
new_df = new_df[~new_df["thai_text"].apply(filter_blank_text)]
new_df = new_df[~new_df["thai_text"].apply(filter_thai_text_without_thai_chars)]

# Save the cleaned dataset
new_df.to_csv('/content/final_cleaned_dataset.csv', index=False)

# Display cleaned data sample
print(new_df.head())
