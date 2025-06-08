import pandas as pd
from textblob import TextBlob
import os

# Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, '..', 'data', 'all_reviews_clean.csv')
output_path = os.path.join(BASE_DIR, '..', 'data', 'all_reviews_with_sentiment.csv')

# Load clean review data
df = pd.read_csv(data_path)

# Define a simple sentiment function
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis
print("🔍 Analyzing sentiment...")
df['sentiment'] = df['review'].apply(get_sentiment)

# Save results
df.to_csv(output_path, index=False)
print(f"✅ Sentiment-labeled data saved to: {output_path}")
print(df[['review', 'sentiment']].head())
