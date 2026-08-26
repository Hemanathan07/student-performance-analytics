# STUDENT PERFORMANCE ANALYTICS
# One clean pipeline combining Phases 4-8:
# Load -> Clean -> Explore (EDA) -> Visualize -> Statistics

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# STEP 1: LOAD DATA (Phase 4 - Pandas)
# -----------------------------
data = {
    "name": ["Asha", "Bala", "Bala", "Cathy", "Dinesh", "Esha", None],
    "python": [80, 72, 72, 91, 65, 88, None],
    "maths": [78, 75, 75, 95, 60, 84, 70],
    "database": [85, 70, 70, 89, 68, 90, 75]
}
df = pd.DataFrame(data)
print("=== RAW DATA ===")
print(df)

# -----------------------------
# STEP 2: CLEAN DATA (Phase 5)
# -----------------------------
df = df.drop_duplicates()
df["python"] = df["python"].fillna(df["python"].median())
df["name"] = df["name"].fillna("Unknown")
for col in ["python", "maths", "database"]:
    df[col] = df[col].clip(0, 100)

print("\n=== CLEANED DATA ===")
print(df)

# -----------------------------
# STEP 3: ANALYZE / EDA (Phase 6)
# -----------------------------
subjects = ["python", "maths", "database"]
df["total"] = df[subjects].sum(axis=1)
df["average"] = df[subjects].mean(axis=1).round(1)

print("\n=== SUBJECT AVERAGES ===")
print(df[subjects].mean())

print("\n=== CORRELATION BETWEEN SUBJECTS ===")
print(df[subjects].corr())

print("\n=== TOP PERFORMERS (average >= 80) ===")
print(df[df["average"] >= 80])

# -----------------------------
# STEP 4: VISUALIZE (Phase 7)
# -----------------------------
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="name", y="average")
plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average")
plt.tight_layout()
plt.savefig("../dashboard/student_averages.png")
plt.show()

plt.figure(figsize=(6, 5))
sns.heatmap(df[subjects + ["average"]].corr(), annot=True, cmap="coolwarm")
plt.title("Marks Correlation Heatmap")
plt.tight_layout()
plt.savefig("../dashboard/correlation_heatmap.png")
plt.show()

# -----------------------------
# STEP 5: STATISTICS (Phase 8)
# -----------------------------
print("\n=== STATISTICS ON AVERAGE MARKS ===")
print("Mean:", df["average"].mean())
print("Median:", df["average"].median())
print("Std Dev:", round(df["average"].std(), 2))
print("Q1:", df["average"].quantile(0.25))
print("Q3:", df["average"].quantile(0.75))

# Save cleaned data for use in SQL / Excel / Dashboard
df.to_csv("../data/students_cleaned.csv", index=False)
print("\nCleaned data saved to ../data/students_cleaned.csv")
