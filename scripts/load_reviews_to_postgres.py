import pandas as pd
import psycopg2

# 1) Load your CSV
df = pd.read_csv('data/all_reviews_with_sentiment.csv')
print(f"🔍 Loaded {len(df)} rows from CSV with columns: {list(df.columns)}")

# 2) Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",        # your host
    database="fintech_reviews", # your database
    user="fintech_user",    # your user
    password="2881",# your password
    port="5432"
)
cursor = conn.cursor()

# 3) Drop & recreate table (safe to run multiple times)
cursor.execute("""
    DROP TABLE IF EXISTS app_reviews;
    CREATE TABLE app_reviews (
        id SERIAL PRIMARY KEY,
        review TEXT,
        rating INTEGER,
        date DATE,
        bank VARCHAR(50),
        source VARCHAR(20),
        sentiment VARCHAR(10)
    );
""")
conn.commit()
print("✅ app_reviews table dropped & re-created.")

# 4) Insert loop
success, fail = 0, 0
for idx, row in df.iterrows():
    try:
        cursor.execute(
            """
            INSERT INTO app_reviews (review, rating, date, bank, source, sentiment)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                row['review'],
                int(row['rating']),
                row['date'],
                row['bank'],
                row['source'],
                row['sentiment']
            )
        )
        success += 1
    except Exception as e:
        print(f"❌ Failed to insert row {idx}: {e}")
        fail += 1

conn.commit()
cursor.close()
conn.close()

print(f"✅ Data upload complete: {success} inserted, {fail} failed.")
