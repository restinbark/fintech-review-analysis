import pandas as pd
import os

# Get current script's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build path to CSV files in ../data/
data_dir = os.path.join(BASE_DIR, '..', 'data')

# ✅ Load each CSV
cbe_df = pd.read_csv(os.path.join(data_dir, 'cbe_reviews.csv'))
boa_df = pd.read_csv(os.path.join(data_dir, 'boa_reviews.csv'))
dashen_df = pd.read_csv(os.path.join(data_dir, 'dashen_reviews.csv'))

# ✅ Combine them
combined_df = pd.concat([cbe_df, boa_df, dashen_df], ignore_index=True)

# ✅ Drop duplicates
before = len(combined_df)
combined_df.drop_duplicates(subset=['review', 'rating', 'date', 'bank'], inplace=True)
after = len(combined_df)
print(f"🧹 Removed {before - after} duplicate reviews.")

# ✅ Drop rows with missing reviews or ratings
combined_df.dropna(subset=['review', 'rating'], inplace=True)

# ✅ Save cleaned data to ../data/
output_path = os.path.join(data_dir, 'all_reviews_clean.csv')
combined_df.to_csv(output_path, index=False)
p
print(f"✅ Cleaned data saved to all_reviews_clean.csv with {len(combined_df)} total reviews.")
