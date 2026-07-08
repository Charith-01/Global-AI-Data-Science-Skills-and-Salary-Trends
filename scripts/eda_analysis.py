from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]

PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
ANALYSIS_TABLES_DIR = PROCESSED_DATA_DIR / "analysis_tables"
CHARTS_DIR = BASE_DIR / "images" / "charts"

ANALYSIS_TABLES_DIR.mkdir(parents=True, exist_ok=True)
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

ai_jobs = pd.read_csv(PROCESSED_DATA_DIR / "ai_jobs_feature_engineered.csv")
skills_demand = pd.read_csv(PROCESSED_DATA_DIR / "skills_demand_cleaned.csv")
country_trends = pd.read_csv(PROCESSED_DATA_DIR / "country_trends_cleaned.csv")

jobs_by_year = ai_jobs.groupby("posted_year")["job_id"].count().reset_index(name="job_count")
jobs_by_country = ai_jobs.groupby("country")["job_id"].count().reset_index(name="job_count")
jobs_by_role = ai_jobs.groupby("role_group")["job_id"].count().reset_index(name="job_count")

salary_by_role = ai_jobs.groupby("role_group")["salary_avg_usd"].mean().reset_index()
salary_by_country = ai_jobs.groupby("country")["salary_avg_usd"].mean().reset_index()
salary_by_career_stage = ai_jobs.groupby("career_stage")["salary_avg_usd"].mean().reset_index()

jobs_by_remote_type = ai_jobs.groupby("remote_type")["job_id"].count().reset_index(name="job_count")
salary_by_remote_type = ai_jobs.groupby("remote_type")["salary_avg_usd"].mean().reset_index()

top_skills = skills_demand.groupby("skill")["job_id"].count().reset_index(name="demand_count")
top_skills = top_skills.sort_values(by="demand_count", ascending=False)

skill_category_demand = skills_demand.groupby("skill_category")["job_id"].count().reset_index(name="demand_count")
skill_level_demand = skills_demand.groupby("skill_level")["job_id"].count().reset_index(name="demand_count")

jobs_by_year.to_csv(ANALYSIS_TABLES_DIR / "jobs_by_year.csv", index=False)
jobs_by_country.to_csv(ANALYSIS_TABLES_DIR / "jobs_by_country.csv", index=False)
jobs_by_role.to_csv(ANALYSIS_TABLES_DIR / "jobs_by_role.csv", index=False)
salary_by_role.to_csv(ANALYSIS_TABLES_DIR / "salary_by_role.csv", index=False)
salary_by_country.to_csv(ANALYSIS_TABLES_DIR / "salary_by_country.csv", index=False)
salary_by_career_stage.to_csv(ANALYSIS_TABLES_DIR / "salary_by_career_stage.csv", index=False)
jobs_by_remote_type.to_csv(ANALYSIS_TABLES_DIR / "jobs_by_remote_type.csv", index=False)
salary_by_remote_type.to_csv(ANALYSIS_TABLES_DIR / "salary_by_remote_type.csv", index=False)
top_skills.to_csv(ANALYSIS_TABLES_DIR / "top_skills.csv", index=False)
skill_category_demand.to_csv(ANALYSIS_TABLES_DIR / "skill_category_demand.csv", index=False)
skill_level_demand.to_csv(ANALYSIS_TABLES_DIR / "skill_level_demand.csv", index=False)

plt.figure(figsize=(8, 5))
plt.plot(jobs_by_year["posted_year"], jobs_by_year["job_count"], marker="o")
plt.title("Jobs by Year")
plt.xlabel("Year")
plt.ylabel("Job Count")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "jobs_by_year.png")
plt.close()

plt.figure(figsize=(8, 5))
jobs_by_country.sort_values("job_count").plot(
    x="country",
    y="job_count",
    kind="barh",
    legend=False
)
plt.title("Jobs by Country")
plt.xlabel("Job Count")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "jobs_by_country.png")
plt.close()

plt.figure(figsize=(8, 5))
top_skills.head(10).sort_values("demand_count").plot(
    x="skill",
    y="demand_count",
    kind="barh",
    legend=False
)
plt.title("Top 10 In-Demand Skills")
plt.xlabel("Demand Count")
plt.ylabel("Skill")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "top_skills.png")
plt.close()

print("EDA tables and charts saved successfully")