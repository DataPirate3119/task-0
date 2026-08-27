import numpy as np

hrss=np.array([8, 14, 24, 20, 2])
atd=np.array([85, 95, 67, 55, 30])
pscores=np.array([67, 83, 53, 80, 70])
fscores=np.array([70, 90, 60, 85, 77])

arr={"Hours Studied": hrss, "Attendance": atd, "Previous Scores": pscores, "Final Scores": fscores}

for n, a in arr.items():
    print(n)
    print("Shape: ", a.shape, "Data Type: ", a.dtype)

meanf=np.mean(fscores)
print("Mean Final Score: ", meanf)

maxf=np.max(fscores)
minf=np.min(fscores)
print("Maximum Score: ", maxf)
print("Minimum Score: ", minf)

stdd=np.std(fscores)
print("Standard Deviation: ", stdd)

bonuss=fscores+5
print("Scores with +5 Bonus: ", bonuss)

al75=fscores>=75
print("Students scoring atleast 75: ", al75)

passeds=fscores[fscores>=75]
print("Scores greater than or equal to 75: ", passeds)
