import pandas as pd
import os

# Create data directory if missing
if not os.path.exists("data"):
    os.makedirs("data")

try:
    # 'latin1' handles encoding issues found in older CSVs
    df = pd.read_csv("data/auto.csv", encoding='latin1')
    
    # Clean underscores immediately
    titles = df["name"].dropna().str.replace("_", " ")
    
    # Save a clean version
    titles.to_csv("data/ebay_titles.csv", index=False, header=["title"])
    print("✅ Step 1: Clean titles saved to 'data/ebay_titles.csv'")
except Exception as e:
    print(f"❌ Error in Data Prep: {e}")