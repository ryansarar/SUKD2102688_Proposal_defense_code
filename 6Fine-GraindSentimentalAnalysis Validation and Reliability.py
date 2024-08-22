import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Load the dataset
file_path = 'output.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
data.head()

# Define a function to classify ratings into sentiment categories
def classify_sentiment_from_rating(rating):
    if rating >= 4:
        return 'POSITIVE'
    elif rating <= 2:
        return 'NEGATIVE'
    else:
        return 'NEUTRAL'

# Apply the function to create a new column with sentiment based on ratings
data['rating_sentiment'] = data['rating'].apply(classify_sentiment_from_rating)

# Since we are only interested in POSITIVE and NEGATIVE sentiments, filter out NEUTRAL sentiments
filtered_data = data[data['rating_sentiment'] != 'NEUTRAL']

# Calculate the confusion matrix
conf_matrix = confusion_matrix(filtered_data['rating_sentiment'], filtered_data['sentiment'])

# Generate classification report
class_report = classification_report(filtered_data['rating_sentiment'], filtered_data['sentiment'])

# Calculate accuracy
accuracy = accuracy_score(filtered_data['rating_sentiment'], filtered_data['sentiment'])

# Print the confusion matrix, classification report, and accuracy
print("Confusion Matrix:")
print(conf_matrix)

print("\nClassification Report:")
print(class_report)

print("\nOverall Accuracy:")
print(accuracy)

# Grouping data by product title to assess internal consistency
grouped_data = filtered_data.groupby('producttitle')['sentiment'].value_counts(normalize=True).unstack().fillna(0)

# Display the grouped data for internal consistency check
print("\nSentiment Distribution by Product Title:")
print(grouped_data)
