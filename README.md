# Fintech App Review Analysis

A data-driven analysis of customer reviews for mobile banking apps in Ethiopia. This project covers data scraping, sentiment analysis, thematic extraction, storage in PostgreSQL, and data visualization using Python.

---

## 🚀 Project Overview

The goal of this project is to analyze customer feedback on the mobile applications of three major Ethiopian banks:

* Commercial Bank of Ethiopia (CBE)
* Bank of Abyssinia (BOA)
* Dashen Bank

We collected reviews from the Google Play Store and processed them to extract insights related to user sentiment, functionality, and satisfaction.

---

## 🧱 Project Structure

```
fintech-review-analysis/
│
├── data/                    # Raw and processed CSV files
├── scripts/                 # Python scripts for scraping, analysis, DB, visualization
├── output/                 # Output charts and plots
├── requirements.txt         # Python dependencies
├── README.md                # Project overview
└── .gitignore               # Files to ignore in Git
```

---

## 📦 Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/restinbark/fintech-review-analysis.git
```

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Make sure PostgreSQL is installed and running. Create a database named `fintech_reviews` and configure a user with full privileges.

---

## 📊 Key Features

### ✅ Task 1: Data Collection and Preprocessing

* Scraped 400 reviews per bank from Google Play using `google-play-scraper`
* Cleaned and standardized dates, ratings, and text fields

### ✅ Task 2: Sentiment & Thematic Analysis

* Used `TextBlob` to label reviews as Positive, Negative, or Neutral
* Applied `TF-IDF` to extract keywords and grouped them into common themes

### ✅ Task 3: Store in PostgreSQL

* Created `app_reviews` table
* Inserted 1190 labeled reviews into the database via Python and `psycopg2`

### ✅ Task 4: Insights & Visualization

* Visualized:

  * Sentiment distribution by bank
  * Average app ratings
  * Weekly review volume
* Charts saved to `/output/`

---

## 🛠 Technologies Used

* Python (pandas, seaborn, matplotlib, psycopg2)
* PostgreSQL + pgAdmin
* Google Play Scraper
* TextBlob

---

## 📁 Output Samples

* `output/sentiment_by_bank.png`
* `output/avg_rating_by_bank.png`
* `output/review_volume_over_time.png`

---

## ✍️ Authors

* **\[Barkilign Mulatu]** – Project Analysis, Code, and Reporting

---

## 📌 License

This project is licensed under the MIT License.
