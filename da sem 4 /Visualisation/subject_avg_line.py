import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('/Users/nehakumari/Desktop/da sem 4 /students_marks_dataset.csv')



subject_avg = df[['Maths', 'Science', 'English']].mean()

# Plot
plt.figure(figsize=(7, 5))
subject_avg.plot(kind='line', marker='o', color='orange')
plt.title('Subject-wise Average Marks')
plt.ylabel('Average Marks')
plt.xticks(rotation=0)
plt.grid(True)
plt.tight_layout()
plt.savefig('subject_avg_line.png')
plt.show()
