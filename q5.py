import pandas as pd

df=pd.read_csv("student_performance.csv")
print(df.head(5))
print("(Rows, Columns): ", df.shape)
print("Column Names: ", list(df.head(0)))
print("Total Missing Values: ", df.isnull().sum().sum())
print("Average Final Score: ", df["Final_Score"].mean())
print("Highest Final Score: \n", df.nlargest(1, "Final_Score"))
df["Improvement"]=df["Final_Score"]-df["Previous_Score"]
print("Students with attendance less than or equal to 80: \n", df[df["Attendance"]>=80])
print("Sorted DataFrame in descending order: \n", df.sort_values(by='Final_Score', ascending=False))

df.to_csv('processed_student_performance.csv')
