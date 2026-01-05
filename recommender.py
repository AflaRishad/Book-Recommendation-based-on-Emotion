import pandas as pd

# Load dataset ONCE
df = pd.read_csv("books_dataset.csv")

def recommend_books(preferences):
    results = df.copy()

    results = results[results["emotion_tags"].str.contains(preferences["emotion"], case=False)]
    results = results[results["mood"] == preferences["mood"]]
    results = results[results["genre"] == preferences["genre"]]
    results = results[results["length"] == preferences["length"]]
    results = results[results["language"] == preferences["language"]]

    return results.head(3)
