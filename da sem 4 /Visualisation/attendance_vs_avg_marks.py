import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/nehakumari/Desktop/da sem 4 /students_marks_dataset.csv')

# Step 1: Create 'Average Marks' column
df['Average Marks'] = df[['Maths', 'Science', 'English']].mean(axis=1)

# Step 2: Plot Attendance vs Average Marks
plt.figure(figsize=(8, 5))
plt.scatter(df['Attendance (%)'], df['Average Marks'], c='green', edgecolors='black')
plt.title('Attendance vs Average Marks')
plt.xlabel('Attendance (%)')
plt.ylabel('Average Marks')
plt.grid(True)
plt.tight_layout()
plt.savefig('attendance_vs_avg_marks.png')
plt.show()
