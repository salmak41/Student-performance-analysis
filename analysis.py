import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_data.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

average_scores = df[['math_score', 'reading_score', 'writing_score']].mean()
print(average_scores)

average_scores.plot(kind='bar')
plt.title("Average Student Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.xticks(
    ticks=range(len(average_scores)),
    labels=['Math', 'Reading', 'Writing'],
    rotation=0
)
plt.tight_layout()
plt.show()

df['average_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

plt.scatter(df['attendance'], df['average_score'])
plt.title("Attendance vs Average Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

sns.boxplot(x='study_time', y='average_score', data=df)
plt.title("Study Time vs Performance")
plt.tight_layout()
plt.show()

gender_avg = df.groupby('gender')['average_score'].mean()
gender_avg.plot(kind='bar')
plt.title("Gender-wise Performance")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()