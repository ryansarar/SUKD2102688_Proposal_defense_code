import pandas as pd
from textblob import TextBlob
import tools
df = pd.read_csv('output.csv')
# Perform fine-grained sentiment analysis on the text column
df['polarity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
# Define a function to categorize polarity into sentiment labels
def categorize_sentiment(polarity):
    if polarity <= -0.5:
        return "Very Negative"
    elif -0.5 < polarity < 0:
        return "Negative"
    elif polarity == 0:
        return "Neutral"
    elif 0 < polarity < 0.5:
        return "Positive"
    else:
        return "Very Positive"
# Apply the function to create a new sentiment category column
df['sentiment_category'] = df['polarity'].apply(categorize_sentiment)
# Display the updated dataframe with the sentiment category
df[['text', 'polarity', 'sentiment_category']].to_csv('newoutput.csv', index=False)