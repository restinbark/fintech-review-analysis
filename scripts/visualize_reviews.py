import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL and load data
conn = psycopg2.connect(
    dbname="fintech_reviews",
    user="fintech_user",
    password="2881",
    host="localhost",
    port="5432"
)

df = pd.read_sql_query("SELECT * FROM app_reviews", conn)
conn.close()

print(f"🔍 Loaded {len(df)} rows from PostgreSQL")

# --- Basic Cleaning ---
df['date'] = pd.to_datetime(df['date'])
# Your plotting code
plt.figure(figsize=(8, 6))
# ...
# --- 1. Sentiment Distribution per Bank ---
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='bank', hue='sentiment')
plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.legend(title="Sentiment")
plt.tight_layout()
plt.savefig("output/sentiment_by_bank.png")
plt.clf()  # clear figure

# --- 2. Average Rating per Bank ---
plt.figure(figsize=(8, 6))
sns.barplot(data=df, x='bank', y='rating', estimator='mean')
plt.title("Average App Rating by Bank")
plt.xlabel("Bank")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.savefig("output/avg_rating_by_bank.png")
plt.clf()

# --- 3. Reviews Over Time (Volume) ---
df['week'] = df['date'].dt.to_period('W').dt.start_time
volume = df.groupby(['week', 'bank']).size().unstack()
volume.plot(figsize=(10, 6))
plt.title("Review Volume Over Time")
plt.xlabel("Date (Week)")
plt.ylabel("Number of Reviews")
plt.legend(title="Bank")
plt.tight_layout()
plt.savefig("output/review_volume_over_time.png")
plt.show()
