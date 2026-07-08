# Global AI & Data Science Job Market, Skills & Salary Trends

## Project Objective

This project analyzes global AI and Data Science job market trends using Python and Power BI. It focuses on job demand, salary patterns, technical skills, career stages, countries, and remote/hybrid/onsite work arrangements.

The final deliverable is an interactive Power BI dashboard supported by a reproducible Python workflow for cleaning, feature engineering, exploratory analysis, chart generation, and dashboard-ready CSV exports.

## Dataset Description

The project uses CSV datasets covering AI and Data Science job postings, skill demand, country-level trends, job title mappings, and dataset metadata.

| Dataset | Description |
|---|---|
| `data/raw/ai_jobs.csv` | Job postings with role, country, salary, experience, industry, company, and work arrangement fields |
| `data/raw/skills_demand.csv` | Skills linked to job postings, categories, and skill levels |
| `data/raw/country_ai_trends.csv` | Country-level job, salary, remote share, and skill trend data |
| `data/raw/job_title_mapping.csv` | Mapping table for grouping job titles |
| `data/raw/data_dictionary.csv` | Column definitions and dataset notes |

## Tools Used

| Area | Tools |
|---|---|
| Programming | Python |
| Analysis | pandas, NumPy |
| Visualization | Matplotlib |
| Dashboard | Power BI Desktop |
| Notebook | Jupyter |
| Version Control | Git, GitHub |

## Workflow

```text
Raw CSV files
-> Data cleaning
-> Feature engineering
-> Exploratory data analysis
-> Chart and analysis table exports
-> Power BI data exports
-> Interactive dashboard
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

```text
charith-01-global-ai-data-science-skills-and-salary-trends/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── country_ai_trends.csv
│   │   ├── data_dictionary.csv
│   │   └── job_title_mapping.csv
│   │
│   └── processed/
│       ├── country_trends_cleaned.csv
│       └── analysis_tables/
│           ├── jobs_by_country.csv
│           ├── jobs_by_year.csv
│           ├── salary_by_country.csv
│           ├── salary_by_role.csv
│           ├── skill_category_demand.csv
│           ├── skill_level_demand.csv
│           └── top_skills.csv
│
├── images/
│   ├── charts/
│   │   ├── jobs_by_country.png
│   │   ├── jobs_by_year.png
│   │   └── top_skills.png
│   │
│   └── dashboard/
│
├── notebooks/
│
├── powerbi/
│   └── data/
│       └── country_trends_powerbi.csv
│
└── scripts/
    ├── data_cleaning.py
    ├── feature_engineering.py
    ├── eda_analysis.py
    └── export_powerbi_data.py
```

---

## Python EDA Visualizations

Python and Matplotlib were used to create exploratory visualizations before developing the Power BI dashboard. These charts helped identify important patterns in job postings, country demand, and skill trends.

### Jobs by Year

![Jobs by Year](images/charts/jobs_by_year.png)

### Salary by Career Stage

![Jobs by Country](images/charts/salary_by_career_stage.png)

### Top In-Demand Skills

![Top Skills](images/charts/top_skills.png)

---

## Power BI Screenshots

### Dashboard Overview

<img width="2767" height="1600" alt="overview" src="https://github.com/user-attachments/assets/96d78c0c-a33e-4b3a-b90b-325b90cfbc9e" />

### Salary Analysis

<img width="2767" height="1600" alt="salary_analysis" src="https://github.com/user-attachments/assets/55c487d9-622b-49c1-b122-4affca5eede3" />

### Skill Analysis

<img width="2767" height="1600" alt="skills_analysis" src="https://github.com/user-attachments/assets/93968586-f39f-4256-bdce-f988bae96a42" />

### Country & Work Arrangement

<img width="2767" height="1600" alt="country_work_arrangement" src="https://github.com/user-attachments/assets/f08054c6-f599-4815-aa68-c1c978e244a2" />

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

## Python EDA Visualizations

Python and Matplotlib were used to create supporting EDA charts before building the Power BI dashboard.

![Jobs by Year](images/charts/jobs_by_year.png)
![Jobs by Country](images/charts/jobs_by_country.png)
![Top Skills](images/charts/top_skills.png)

## Dashboard Pages

The Power BI dashboard includes four pages:

| Page | Focus |
|---|---|
| Overview | Job volume, countries, salary summary, yearly trend, work arrangement mix |
| Salary Analysis | Salary by year, role group, career stage, country, and work arrangement |
| Skills Analysis | Top skills, skill categories, skill levels, and skill demand patterns |
| Country & Work Arrangement | Country comparisons, remote share, salary, and job distribution |

## Main Insights

- AI and Data Science jobs show broad global demand across multiple countries.
- Python, SQL, cloud platforms, machine learning frameworks, and NLP-related skills appear strongly in the skills data.
- Senior-level roles generally show higher average salaries than entry-level and mid-level roles.
- Remote, hybrid, and onsite work arrangements all remain relevant in the job market.
- Country-level analysis helps compare job availability, salary differences, and work arrangement patterns.

## Screenshots

### Overview

![Overview Dashboard](images/dashboard/overview.png)

### Salary Analysis

![Salary Analysis Dashboard](images/dashboard/salary_analysis.png)

### Skills Analysis

![Skills Analysis Dashboard](images/dashboard/skills_analysis.png)

### Country & Work Arrangement

![Country and Work Arrangement Dashboard](images/dashboard/country_work_arrangement.png)

## How to Run the Project

1. Clone the repository.

```bash
git clone https://github.com/your-username/global-ai-data-science-skills-salary-trends.git
cd global-ai-data-science-skills-salary-trends
```

2. Create and activate a virtual environment.

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Run the pipeline from the project root.

```bash
python scripts/data_cleaning.py
python scripts/feature_engineering.py
python scripts/eda_analysis.py
python scripts/export_powerbi_data.py
```

5. Open the Power BI dashboard.

```text
powerbi/AI_Data_Science_Job_Market_Dashboard.pbix
```

## Folder Structure

```text
charith-01-global-ai-data-science-skills-and-salary-trends/
|-- README.md
|-- requirements.txt
|-- data/
|   |-- raw/
|   |-- processed/
|   |   |-- analysis_tables/
|-- images/
|   |-- charts/
|   |-- dashboard/
|-- notebooks/
|-- powerbi/
|   |-- data/
|-- scripts/
|   |-- data_cleaning.py
|   |-- feature_engineering.py
|   |-- eda_analysis.py
|   |-- export_powerbi_data.py
```

## Project Outcome

This project demonstrates an end-to-end analytics workflow from raw CSV files to a Power BI dashboard. It is designed as a portfolio project showing data preparation, exploratory analysis, dashboard data modeling support, and insight communication.
