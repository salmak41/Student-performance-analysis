# Student Performance Analytics Dashboard

A Python-based data analysis project to study student academic performance using exploratory data analysis techniques.

## Overview
This project focuses on analyzing student academic data to identify patterns related to subject-wise performance, attendance, study habits, and gender-based trends. It demonstrates practical application of Python for data cleaning, analysis, and visualization, making it suitable for internships and entry-level roles.

## Problem Statement
Educational institutions collect large amounts of student performance data, but meaningful insights are often not extracted. This project aims to analyze such data and present clear insights that can help understand factors influencing academic performance.

## Objectives
- Analyze academic performance across subjects
- Understand the impact of attendance on scores
- Study the relationship between study time and performance
- Compare performance across gender groups
- Present insights using clear visualizations

## Dataset
The dataset (`student_data.csv`) includes the following attributes:
- math_score: Mathematics score
- reading_score: Reading score
- writing_score: Writing score
- attendance: Attendance percentage
- study_time: Daily study time
- gender: Student gender

Missing numeric values are handled using mean imputation.

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code

## Key Features
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering (average score per student)
- Subject-wise and demographic performance analysis
- Data visualization for insight generation

## Visualizations
- Bar chart for average scores by subject
- Scatter plot for attendance vs average score
- Box plot for study time vs academic performance
- Bar chart for gender-wise performance comparison

## Project Structure
student-performance-analysis/
│
├── student_data.csv
├── analysis.py
├── README.md
└── requirements.txt

## How to Run the Project
1. Clone the repository
2. Navigate to the project directory
   cd student-performance-analysis
3. Install required libraries
   pip install pandas numpy matplotlib seaborn
4.Run the Python script
   python analysis.py
   
## Results and Insights
- Students with higher attendance generally perform better
- Consistent study time positively impacts average scores
- Performance shows slight variation across gender groups
- Reading scores are generally higher compared to math scores

## Future Enhancements
- Add machine learning models for performance prediction
- Create interactive dashboards using Streamlit or Power BI
- Expand the dataset for deeper analysis
- Automate report generation

## Why This Project Matters
This project demonstrates practical data analysis skills, analytical thinking, and clean coding practices, providing a strong foundation for Python and Data Analyst internship roles.

