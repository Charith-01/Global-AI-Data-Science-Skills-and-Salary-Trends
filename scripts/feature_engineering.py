from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

ai_jobs = pd.read_csv(PROCESSED_DATA_DIR / "ai_jobs_cleaned.csv")

ai_jobs["salary_avg_usd"] = (
    ai_jobs["salary_min_usd"] + ai_jobs["salary_max_usd"]
) / 2

ai_jobs["salary_level"] = pd.cut(
    ai_jobs["salary_avg_usd"],
    bins=[0, 80000, 120000, 160000, np.inf],
    labels=["Low", "Medium", "High", "Very High"]
)

def map_career_stage(experience):
    experience = str(experience).lower()

    if "entry" in experience or "junior" in experience:
        return "Entry Level"
    elif "mid" in experience:
        return "Mid Level"
    elif "senior" in experience or "lead" in experience:
        return "Senior Level"
    else:
        return "Other"

ai_jobs["career_stage"] = ai_jobs["experience_level"].apply(map_career_stage)

ai_jobs["is_remote_friendly"] = ai_jobs["remote_type"].isin(["Remote", "Hybrid"])

def map_role_group(title):
    title = str(title).lower()

    if "data scientist" in title:
        return "Data Science"
    elif "machine learning" in title or "ml" in title:
        return "Machine Learning"
    elif "data analyst" in title or "analytics" in title:
        return "Data Analytics"
    elif "ai research" in title or "research" in title:
        return "AI Research"
    elif "mlops" in title or "machine learning engineer" in title:
        return "MLOps"
    else:
        return "Applied AI / Research"

ai_jobs["role_group"] = ai_jobs["job_title"].apply(map_role_group)

ai_jobs.to_csv(PROCESSED_DATA_DIR / "ai_jobs_feature_engineered.csv", index=False)

print("Feature engineering completed successfully")
print(ai_jobs[[
    "job_title",
    "role_group",
    "experience_level",
    "career_stage",
    "remote_type",
    "is_remote_friendly",
    "salary_avg_usd",
    "salary_level"
]].head())