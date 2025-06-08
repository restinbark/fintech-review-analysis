from google_play_scraper import Sort, reviews
import pandas as pd

# 🏦 Bank apps and IDs
bank_apps = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp'
}

# Loop through each bank and scrape reviews
for bank, app_id in bank_apps.items():
    print(f"\n🔄 Fetching reviews for {bank} ({app_id})...")

    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='et',
            sort=Sort.NEWEST,
            count=400,
            filter_score_with=None
        )

        df = pd.DataFrame(result)

        if df.empty:
            print(f"⚠️ No data returned for {bank}")
            continue

        # Check expected columns
        required = {'content', 'score', 'at'}
        if not required.issubset(df.columns):
            print(f"⚠️ Missing expected fields for {bank}: {required - set(df.columns)}")
            continue

        # Keep and rename columns
        df = df[['content', 'score', 'at']]
        df.rename(columns={'content': 'review', 'score': 'rating', 'at': 'date'}, inplace=True)

        # Add metadata
        df['bank'] = bank
        df['source'] = 'Google Play'
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

        # Save to CSV
        filename = f"{bank.lower()}_reviews.csv"
        df.to_csv(filename, index=False)
        print(f"✅ Saved {len(df)} reviews to {filename}")

    except Exception as e:
        print(f"❌ Error fetching reviews for {bank}: {e}")
