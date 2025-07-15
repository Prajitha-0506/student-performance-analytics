# Project 2: Student Performance Analytics Dashboard

## Problem Statement
Many students struggle academically or mentally during their academic journey, increasing their risk of dropping out. Educational institutions need an effective way to identify such students early to provide timely interventions.

## Objective
Analyze behavioral and academic data to:
- Discover key patterns related to dropout risk.
- Understand how GPA, attendance, and mental health impact performance.
- Identify students who are most at risk and visualize critical trends.

import pandas as pd

 
df = pd.read_csv("C:/Users/Asus/Downloads/RISE/student_management_dataset.csv")
## Dataset Overview
The dataset contains data for 1000 students, including:
- Academic metrics: GPA, course performance, credits
- Behavioral metrics: attendance rate, class participation, online learning time
- Well-being indicators: mental health score, social engagement
- Risk classification: dropout risk flag (1 = at risk, 0 = not at risk)

df.head()
df.info()
df.describe()
df.isnull().sum()

## Correlation Analysis
We use a correlation matrix and heatmap to identify relationships between variables. This helps in understanding which factors influence dropout risk the most.

cols = ['GPA', 'Attendance_Rate', 'Online_Learning_Hours', 
        'Library_Usage_Hours', 'Class_Participation_Score', 
        'Mental_Health_Score', 'Dropout_Risk']
df[cols].corr()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

## Visual Analysis

To support our numeric findings, we created the following visualizations:

- **Boxplot**: GPA distribution by dropout status
- **Scatter plot**: Attendance vs GPA, colored by risk
- **Histogram**: Mental health scores for at-risk vs non-risk groups

sns.boxplot(x='Dropout_Risk', y='GPA', data=df)
plt.title("GPA Distribution by Dropout Risk")
plt.xlabel("Dropout Risk")
plt.ylabel("GPA")
plt.show()

sns.scatterplot(x='Attendance_Rate', y='GPA', hue='Dropout_Risk', data=df)
plt.title("Attendance vs GPA (colored by Dropout Risk)")
plt.xlabel("Attendance Rate (%)")
plt.ylabel("GPA")
plt.show()

sns.histplot(data=df, x='Mental_Health_Score', hue='Dropout_Risk', multiple='stack', bins=10)
plt.title("Mental Health Score Distribution by Dropout Risk")
plt.xlabel("Mental Health Score")
plt.ylabel("Student Count")
plt.show()

## Custom At-Risk Flag Creation

While the dataset contains a `Dropout_Risk` column, we created our own `At_Risk_Flag` using logic:
- GPA < 2.0
- OR Attendance Rate < 60%
- OR Mental Health Score < 5

df['At_Risk_Flag'] = (
    (df['GPA'] < 2.0) | 
    (df['Attendance_Rate'] < 60) | 
    (df['Mental_Health_Score'] < 5)
).astype(int)

df['At_Risk_Flag'].value_counts()

df[df['At_Risk_Flag'] == 1].head()

## Conclusion

This project aimed to explore patterns and signals of dropout risk among students using academic, behavioral, and well-being data.

### Key Findings:

- **GPA** had the strongest negative correlation with dropout risk (-0.18).
- **Mental Health Score** showed a moderate negative relationship (-0.15).
- **Attendance Rate** contributed to risk but with weak correlation (-0.11).
- **Engagement metrics** like participation or online learning showed minimal impact on dropout prediction.

### Custom Risk Detection:

Our custom flag, based on GPA, attendance, and mental health, offers a more proactive approach for identifying vulnerable students — even before institutional systems might notice.

## Recommendations

- Offer academic mentoring and tutoring to students with GPA below 2.0.
- Provide mental health counseling and peer support groups to those scoring low on wellness.
- Monitor attendance and automate early alerts when students dip below a 60% threshold.
- Combine academic and emotional metrics to form a holistic view of student well-being.

## Final Note

With this dashboard and logic, educational institutions can make data-informed decisions and offer personalized support — not just to improve retention, but to transform the student experience.
