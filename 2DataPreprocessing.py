import string
from bs4 import BeautifulSoup
import re
import nltk
nltk.download('punkt')
import nltk
nltk.download('stopwords')
import nltk
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer #scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer #scikit-learn
import pandas as pd
import numpy as np
# 1. Text Cleaning
def remove_html_tags(text):
    return BeautifulSoup(text, "html.parser").get_text()
def to_lowercase(text):
    return text.lower()
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
def remove_numbers(text):
    return ''.join([i for i in text if not i.isdigit()])
def remove_extra_whitespace(text):
    return ' '.join(text.split())
def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z\s]', '', text)
# 2 Tokenization: Tokenization is the process of breaking down text into individual words or tokens.
# Word tokenization: Split text into words.
def tokenize(text):
    return word_tokenize(text)
# 3. Stop Words Removal : Stop words are common words that do not carry significant meaning and can be removed to reduce the dimensionality of the text.
# Remove stop words:
def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]
# 4. Stemming and Lemmatization : Stemming and lemmatization reduce words to their root form, which helps in reducing the vocabulary size.
# Stemming:
def stem_tokens(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in tokens]
# Lemmatization:
def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]
# 5. Handling Negations: Negations can flip the sentiment of the words that follow them. Handling negations is essential for accurate sentiment analysis.
# Negation handling:
def handle_negations(tokens):
    negations = ["not", "no", "never"]
    transformed_tokens = []
    negation = False
    for token in tokens:
        if negation:
            token = "NOT_" + token
        if token in negations:
            negation = True
        else:
            negation = False
        transformed_tokens.append(token)
    return transformed_tokens
# 6. Putting It All Together: Combining all the preprocessing steps into a single function:
def preprocess_text(text):
    text = remove_html_tags(text)
    text = to_lowercase(text)
    text = remove_punctuation(text)
    text = remove_numbers(text)
    text = remove_extra_whitespace(text)
    text = remove_special_characters(text)
    tokens = tokenize(text)
    tokens = remove_stop_words(tokens)
    tokens = lemmatize_tokens(tokens)
    tokens = handle_negations(tokens)
    return ' '.join(tokens)
# Main fuction 
def main():
    data = pd.read_excel('output.xlsx')
    texts = "\n".join(data["review"]).split("\n")
    title = "\n".join(data["title"]).replace("s_x000D_\n", "s ").split("\n")
    rating = "\n".join(data["rating"]).split("\n")
    data = data.drop('title', axis=1)
    data = data.drop('rating', axis=1)
    c11=0
    a = texts
    for cc in texts :
        rating[c11] = ""+rating[c11]
        title[c11] = ""+title[c11]
        title[c11] = title[c11].replace(rating[c11], "").strip()
        rating[c11]= rating[c11].replace("out of 5 stars", "").strip()
        a[c11] = preprocess_text( title[c11] +" "+texts[c11])
        print("Here is The result:"+str(c11)+"\n"+ a[c11])
        print("Here is no 11111:\n"+ title[c11])
        c11 +=1
    annotated_data = pd.DataFrame(a)
    data.insert(1, "title",title)
    data.insert(2, "rating",rating)
    data.insert(4, "text",annotated_data)
    data.to_csv('output.csv', index=False)
main()


