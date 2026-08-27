import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("processed_student_performance.csv")

plt.figure()
plt.bar(df["Student"], df["Final_Score"])
plt.xlabel("Student Name")
plt.ylabel("Final Score")
plt.title("Student names vs Final scores")
plt.xticks(rotation=45)
plt.savefig("final_scores.png")
plt.show()

plt.figure()
plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.title("Hours studied vs Final score")
plt.savefig("study_vs_score.png")
plt.show()

plt.figure()
plt.hist(df["Final_Score"], bins=5)
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.title("Distribution of final scores")
plt.savefig("score_distribution.png")
plt.show()

plt.figure()
plt.scatter(df["Attendance"], df["Final_Score"])
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.title("Attendance vs Final Score") #0AttendancePolicy
plt.savefig("bits_plot.png")
plt.show()
