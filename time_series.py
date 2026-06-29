import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel("student_data.xlsx")

# Create Month column
df["Month"] = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct",
               "Nov","Dec","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]

# Create Sales column using Exam Score
df["Sales"] = df["Study_Hours"]

# ----- Line Chart -----
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("line_chart.png")
plt.close()

# ----- Bar Chart -----
attendance = {
    "Low": len(df[df["Attendance"] < 80]),
    "Medium": len(df[(df["Attendance"] >= 80) & (df["Attendance"] < 90)]),
    "High": len(df[df["Attendance"] >= 90])
}

plt.figure(figsize=(6,5))
plt.bar(attendance.keys(), attendance.values())
plt.title("Attendance Categories")
plt.xlabel("Category")
plt.ylabel("Students")
plt.savefig("bar_chart.png")
plt.close()

# ----- Pie Chart -----
plt.figure(figsize=(6,6))
plt.pie(attendance.values(), labels=attendance.keys(), autopct="%1.1f%%")
plt.title("Attendance Share")
plt.savefig("pie_chart.png")
plt.close()

# ----- Summary -----
summary = df.describe()
summary.to_csv("summary.csv")

print("Project Completed Successfully!")