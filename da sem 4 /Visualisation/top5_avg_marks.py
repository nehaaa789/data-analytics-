import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('/Users/nehakumari/Desktop/da sem 4 /students_marks_dataset.csv')

# Calculate average marks
df['Average Marks'] = df[['Maths', 'Science', 'English']].mean(axis=1)

# Sort and select top 5
top5 = df.sort_values(by='Average Marks', ascending=False).head(5)

# Plot
plt.figure(figsize=(8, 5))
plt.bar(top5['Name'], top5['Average Marks'], color='skyblue')
plt.title('Top 5 Students by Average Marks')
plt.ylabel('Average Marks')
plt.xlabel('Student Name')
plt.tight_layout()
plt.savefig('top5_avg_marks.png')
plt.show()

