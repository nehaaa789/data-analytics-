import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/nehakumari/Desktop/da sem 4 /students_marks_dataset.csv')

plt.figure(figsize=(9, 5))
df[['Maths', 'Science', 'English']].plot(kind='hist', bins=10, alpha=0.5)
plt.title('Distribution of Marks in All Subjects')
plt.xlabel('Marks')
plt.grid(True)
plt.tight_layout()
plt.savefig('marks_distribution.png')
plt.show()
