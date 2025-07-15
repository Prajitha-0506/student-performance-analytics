# 🎓 Student Analytics Dashboard (CLI-Based – Python & Pandas)

## 📌 Project Description

This project focuses on analyzing academic, behavioral, and well-being data to **identify students at risk of dropping out**. Using a command-line Python application and data visualizations, the dashboard provides meaningful insights into factors affecting student performance and risk.

Built with Pandas, Seaborn, and Matplotlib, the tool enables educational institutions to **spot early warning signs** using GPA, attendance, and mental health metrics.

---

## 🎯 Objectives

- Discover key patterns related to dropout risk  
- Analyze correlations between academic performance and well-being  
- Develop a custom at-risk detection flag  
- Visualize critical trends using Python plots  
- Support early interventions for vulnerable students

---

## 🧾 Dataset Overview

- **Rows**: 1000 students  
- **Features**:
  - `GPA`, `Credits`, `Course_Performance`
  - `Attendance_Rate`, `Class_Participation`, `Online_Learning_Hours`
  - `Mental_Health_Score`, `Social_Engagement`
  - `Dropout_Risk`: 1 = at risk, 0 = not at risk

📍 *Loaded using:*
```python
df = pd.read_csv("student_management_dataset.csv")


📊 Key Analyses & Visualizations
✅ Correlation Heatmap
sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm')
✅ GPA vs Dropout Risk (Boxplot)
sns.boxplot(x='Dropout_Risk', y='GPA', data=df)
✅ Attendance vs GPA (Scatter)
sns.scatterplot(x='Attendance_Rate', y='GPA', hue='Dropout_Risk', data=df)
✅ Mental Health Score (Histogram)
sns.histplot(data=df, x='Mental_Health_Score', hue='Dropout_Risk', multiple='stack')


🚨 Custom At-Risk Detection
In addition to the dataset's Dropout_Risk flag, we implemented a custom At_Risk_Flag:
df['At_Risk_Flag'] = (
    (df['GPA'] < 2.0) |
    (df['Attendance_Rate'] < 60) |
    (df['Mental_Health_Score'] < 5)
).astype(int)
This logic helps flag students even before institutional metrics mark them at risk.


🧠 Key Findings
📉 GPA has the strongest negative correlation with dropout risk (-0.18)
🧠 Mental health scores are moderately correlated (-0.15)
📚 Attendance shows weak correlation but still relevant (-0.11)
⚠️ Engagement metrics had limited predictive power


💡 Recommendations
Provide academic support for students with GPA < 2.0
Offer mental wellness programs for low scoring students
Monitor attendance and trigger alerts when < 60%
Use a combined academic + behavioral approach to intervention


🛠️ Tools & Technologies
🐍 Python 3
📊 Pandas, Seaborn, Matplotlib
📁 CSV data input
💻 Jupyter Notebook / CLI interface


🙋‍♀️ Author
Tammana Prajitha
📧 prajithatammana@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/tammana-prajitha-24a5ab298/)

📌 Project Type
💼 Internship Project at RISE (June 2025)
🔍 Focus: Data Analysis, Risk Detection, Visualization
