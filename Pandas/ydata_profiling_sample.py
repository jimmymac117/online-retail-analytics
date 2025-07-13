#encoding="latin1"
import pandas as pd
from ydata_profiling import ProfileReport

# Load your dataset (CSV as an example)
df = pd.read_csv("/Users/jimmcgrail/Desktop/data.csv", encoding="latin1")  # Replace with your file path

# Basic data checks
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

# Create the profile report
profile = ProfileReport(df, title="Data Profiling Report", explorative=True)

# Export the report to HTML
profile.to_file("data_profiling_report.html")

print("Data profiling report saved as 'data_profiling_report.html'")
import os
print("Saved to:", os.getcwd())