# Global AI & Data Science Job Market, Skills & Salary Trends Dashboard

## Project Overview

This project analyzes the global AI and Data Science job market using job posting, salary, skill demand, country trend, and work arrangement data. The main objective is to identify job market trends, high-demand skills, salary patterns, career-stage differences, and remote/hybrid/onsite work opportunities across different countries.

The final output of this project is an interactive Power BI dashboard supported by Python-based data cleaning, feature engineering, exploratory data analysis, and prepared dashboard datasets.

---

## Project Objective

The objective of this project is to:

- Analyze global AI and Data Science job market trends.
- Identify the most in-demand technical skills.
- Compare salary patterns across roles, countries, and career stages.
- Understand remote, hybrid, and onsite work arrangement trends.
- Build an interactive Power BI dashboard for clear business insights.
- Demonstrate a complete analytics workflow from raw data to dashboard reporting.

---

## Dataset Description

The project uses a global AI and Data Science job market dataset containing job postings, salary information, skill demand, country-level AI trends, and job title mapping details.

Main datasets used:

| Dataset | Description |
|---|---|
| `ai_jobs.csv` | Main job posting dataset containing job titles, countries, salaries, experience levels, industries, company details, and work arrangements |
| `skills_demand.csv` | Skill demand dataset showing skills linked to job postings |
| `country_ai_trends.csv` | Country-level AI job trends, salary, remote percentage, and top skill information |
| `job_title_mapping.csv` | Job title mapping reference data |
| `data_dictionary.csv` | Dataset column definitions and descriptions |

---

## Tools and Technologies Used

| Category | Tools |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Power BI |
| Dashboard Development | Power BI Desktop |
| Notebook Environment | Jupyter Notebook / VS Code |
| Version Control | Git, GitHub |
| Data Format | CSV |

---

## Project Workflow

The project follows a complete data analytics workflow:

```text
Raw Data
   ↓
Data Loading
   ↓
Data Cleaning and Validation
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Chart and Table Export
   ↓
Power BI Data Preparation
   ↓
Interactive Dashboard Development
   ↓
Insights and Reporting
```

### 1. Data Loading and Cleaning

The raw datasets were loaded using Python and checked for:
 - Dataset shape
 - Missing values
 - Duplicate records
 - Data types
 - Salary value consistency
 - Basic data quality issues

### 2. Feature Engineering

New analytical columns were created to support dashboard insights:

| Feature              | Purpose                                                          |
| -------------------- | ---------------------------------------------------------------- |
| `salary_avg_usd`     | Average salary calculated from minimum and maximum salary        |
| `salary_level`       | Salary category such as Low, Medium, High, and Very High         |
| `career_stage`       | Career grouping such as Entry Level, Mid Level, and Senior Level |
| `is_remote_friendly` | Identifies Remote and Hybrid jobs                                |
| `role_group`         | Groups detailed job titles into broader role categories          |

### 3. Exploratory Data Analysis

EDA was performed to analyze:
 - Job trends by year
 - Job distribution by country
 - Job distribution by role group
 - Salary trends by year
 - Salary by country
 - Salary by career stage
 - Salary by role group
 - Work arrangement distribution
 - Top in-demand skills
 - Skill category distribution
 - Skill level distribution

### 4. Power BI Data Export

Cleaned and feature-engineered datasets were exported for Power BI:

```
powerbi/data/ai_jobs_powerbi.csv
powerbi/data/skills_demand_powerbi.csv
powerbi/data/country_trends_powerbi.csv
```
---

## Dashboard Pages

The Power BI dashboard contains four main pages.

### 1. Overview

This page provides a high-level summary of the AI and Data Science job market.

Main visuals:
 - Total Jobs
 - Average Salary
 - Total Countries
 - Total Skills
 - Job Count Trend by Year
 - Jobs by Country
 - Work Arrangement Distribution

### 2. Salary Analysis

This page focuses on salary patterns across years, roles, career stages, and work arrangements.

Main visuals:
 - Average Salary
 - Highest Salary
 - Lowest Salary
 - Salary Range
 - Average Salary Trend by Year
 - Average Salary by Career Stage
 - Average Salary by Role Group
 - Average Salary by Work Arrangement
 - Job Distribution by Salary Level

### 3. Skills Analysis

This page analyzes skill demand across AI and Data Science roles.

Main visuals:
 - Total Skills
 - Top Skill
 - Top Skill Category
 - Most Common Skill Level
 - Top 10 In-Demand Skills
 - Skill Category Distribution
 - Skill Level Distribution
 - Skill Category Mix by Role Group

### 4. Country & Work Arrangement Analysis

This page compares job availability, salary, and work arrangement patterns across countries.

Main visuals:
 - Total Countries
 - Top Country
 - Highest Average Salary Country
 - Remote Job Share
 - Jobs by Country
 - Average Salary by Country
 - Work Arrangement by Country
 - Country Job Trend by Year

---

## Main Insights

Key insights identified from the analysis:
 - AI and Data Science job postings show consistent global demand across multiple countries.
 - AWS, GCP, TensorFlow, Azure, Scikit-learn, Python, SQL, and NLP appear among the most in-demand skills.
 - Machine Learning related skills represent the largest skill category in the dataset.
 - Salary patterns vary by career stage, with senior-level roles showing higher average salary values.
 - Remote, hybrid, and onsite work arrangements are all important in the AI and Data Science job market.
 - Country-level analysis helps compare job availability and salary differences across major markets.
 - Role groups such as Data Science, Machine Learning, Data Analytics, AI Research, and MLOps show strong demand.

---

## Project Folder Structure

```
global-ai-data-science-skills-salary-trends/
│
├── data/
│   ├── raw/
│   │   ├── ai_jobs.csv
│   │   ├── skills_demand.csv
│   │   ├── country_ai_trends.csv
│   │   ├── job_title_mapping.csv
│   │   └── data_dictionary.csv
│   │
│   └── processed/
│       ├── ai_jobs_cleaned.csv
│       ├── skills_demand_cleaned.csv
│       ├── country_trends_cleaned.csv
│       ├── ai_jobs_feature_engineered.csv
│       └── analysis_tables/
│
├── images/
│   └── charts/
│       ├── jobs_by_year.png
│       ├── jobs_by_country.png
│       ├── salary_by_year.png
│       ├── top_skills.png
│       └── skill_category_distribution.png
│
├── notebooks/
│   └── ai_data_science_job_market_analysis.ipynb
│
├── powerbi/
│   ├── data/
│   │   ├── ai_jobs_powerbi.csv
│   │   ├── skills_demand_powerbi.csv
│   │   └── country_trends_powerbi.csv
│   │
│   └── AI_Data_Science_Job_Market_Dashboard.pbix
│
├── scripts/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── eda_analysis.py
│   └── export_powerbi_data.py
│
├── README.md
└── requirements.txt
```

---

## Screenshots


---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/global-ai-data-science-skills-salary-trends.git
cd global-ai-data-science-skills-salary-trends
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

For Windows:
```bash
venv\Scripts\activate
```

For macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run Python Scripts

Run the scripts in this order:

```bash
python scripts/data_cleaning.py
python scripts/feature_engineering.py
python scripts/eda_analysis.py
python scripts/export_powerbi_data.py
```

### 5. Open Power BI Dashboard

Open the Power BI file:

```
powerbi/AI_Data_Science_Job_Market_Dashboard.pbix
```

Then refresh the data in Power BI if required.

---

## Project Outcome

This project demonstrates an end-to-end data analytics workflow using Python and Power BI. It covers data cleaning, feature engineering, exploratory analysis, dashboard preparation, interactive visualization, and insight generation.

The final dashboard helps users understand global AI and Data Science job market trends, salary patterns, skill demand, and work arrangement opportunities.