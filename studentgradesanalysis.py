import pandas as pd


data = {

    'student' : ['Tom', 'Nick', 'John', 'Tom', 'Nick', 'John', 'Tom', 'Nick', 'John'],
    'subject' : ['Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'History', 'History', 'History'],
    'grade' : [85, 88, 92, 78, 89, 90, 85, 88, 92]
}

df = pd.DataFrame(data)

high_scores = df[df['grade'] > 80]

print("Students with grades above 80:\n", high_scores)

average_grade = df.groupby('subject')['grade'].mean()
print("\nAverage grade for each subject:\n", average_grade)