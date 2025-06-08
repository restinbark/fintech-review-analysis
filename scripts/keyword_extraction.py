import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

# Load sentiment-labeled reviews
df = pd.read_csv('data/all_reviews_with_sentiment.csv')

# Clean the text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)  # keep letters and spaces only
    return text

df['cleaned_review'] = df['review'].apply(clean_text)

# Get English stopwords
stop_words = stopwords.words('english')

# TF-IDF extraction
vectorizer = TfidfVectorizer(max_features=30, stop_words=stop_words)
X = vectorizer.fit_transform(df['cleaned_review'])

# Get top keywords
keywords = vectorizer.get_feature_names_out()
print("🔑 Top Keywords:")
print(keywords)

# Save to CSV
pd.DataFrame({'top_keywords': keywords}).to_csv('data/top_keywords.csv', index=False)
print("✅ Top keywords saved to data/top_keywords.csv")
