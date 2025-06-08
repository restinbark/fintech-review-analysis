import pandas as pd

# Load top keywords
keywords_df = pd.read_csv('data/top_keywords.csv')

# Example theme mapping (edit as needed)
theme_map = {
    'login': 'Login Issues',
    'error': 'Login Issues',
    'password': 'Login Issues',
    'slow': 'Performance',
    'crash': 'Performance',
    'freeze': 'Performance',
    'ui': 'User Experience',
    'design': 'User Experience',
    'navigation': 'User Experience',
    'atm': 'Feature Request',
    'fingerprint': 'Feature Request',
    'feature': 'Feature Request',
    'support': 'Customer Service',
    'help': 'Customer Service'
}

# Match each keyword to a theme
keywords_df['theme'] = keywords_df['top_keywords'].map(theme_map).fillna('Other')

# Save grouped results
keywords_df.to_csv('data/keywords_with_themes.csv', index=False)
print("✅ Saved keyword-theme mapping to data/keywords_with_themes.csv")
