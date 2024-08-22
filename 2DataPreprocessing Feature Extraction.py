import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Load your CSV file
df = pd.read_csv('output.csv')

# Initialize the Count Vectorizer
vectorizer = CountVectorizer()

# Fit and transform the text data
X_bow = vectorizer.fit_transform(df['text'])

# Convert the result to a DataFrame for better readability
bow_df = pd.DataFrame(X_bow.toarray(), columns=vectorizer.get_feature_names_out())

# Display the first few rows of the BoW DataFrame
print(bow_df.head())
