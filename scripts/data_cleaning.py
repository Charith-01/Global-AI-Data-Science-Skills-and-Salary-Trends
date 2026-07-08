from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

ai_jobs = pd.read_csv(RAW_DATA_DIR / "ai_jobs.csv")
skills_demand = pd.read_csv(RAW_DATA_DIR / "skills_demand.csv")
country_trends = pd.read_csv(RAW_DATA_DIR / "country_ai_trends.csv")

print("Data loaded successfully")
print("AI Jobs Shape:", ai_jobs.shape)
print("Skills Demand Shape:", skills_demand.shape)
print("Country Trends Shape:", country_trends.shape)

print("\nMissing values in AI Jobs:")
print(ai_jobs.isnull().sum())

print("\nDuplicate rows:")
print("AI Jobs:", ai_jobs.duplicated().sum())
print("Skills Demand:", skills_demand.duplicated().sum())
print("Country Trends:", country_trends.duplicated().sum())

ai_jobs.to_csv(PROCESSED_DATA_DIR / "ai_jobs_cleaned.csv", index=False)
skills_demand.to_csv(PROCESSED_DATA_DIR / "skills_demand_cleaned.csv", index=False)
country_trends.to_csv(PROCESSED_DATA_DIR / "country_trends_cleaned.csv", index=False)

print("\nCleaned CSV files saved successfully")