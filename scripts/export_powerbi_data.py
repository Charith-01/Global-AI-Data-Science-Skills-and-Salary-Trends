from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
POWERBI_DATA_DIR = BASE_DIR / "powerbi" / "data"

POWERBI_DATA_DIR.mkdir(parents=True, exist_ok=True)

ai_jobs = pd.read_csv(PROCESSED_DATA_DIR / "ai_jobs_feature_engineered.csv")
skills_demand = pd.read_csv(PROCESSED_DATA_DIR / "skills_demand_cleaned.csv")
country_trends = pd.read_csv(PROCESSED_DATA_DIR / "country_trends_cleaned.csv")

ai_jobs.to_csv(POWERBI_DATA_DIR / "ai_jobs_powerbi.csv", index=False)
skills_demand.to_csv(POWERBI_DATA_DIR / "skills_demand_powerbi.csv", index=False)
country_trends.to_csv(POWERBI_DATA_DIR / "country_trends_powerbi.csv", index=False)

print("Power BI data files exported successfully")
print("Files saved to:", POWERBI_DATA_DIR)