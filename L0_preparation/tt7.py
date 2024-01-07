import pandas as pd
import numpy as np


# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.

morg_df = pd.read_csv("data/morg_d07_strings.csv", index_col="h_id")

morg_df

# TASKS 2-6
# For each of the tasks, print the value requested in the task.

age_col = morg_df["age"]
age_col

h_id_1_2_2 = morg_df.loc["1_2_2"]
first_four = morg_df[:4]
h_id_1_2_2, first_four

fill_cols = {}
for col in morg_df.columns:
    if any(morg_df[col].isna()):
        fill_cols[col] = 0.0

morg_df.fillna(value=fill_cols, inplace=True)

morg_df
# Task 7
# convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

for cat in TO_CATEGORICALS:
    morg_df[cat] = morg_df[cat].astype("category")

morg_df

# Example use of cut()
boundaries = range(16, 89, 8)
morg_df.loc[:, "age_bin"] = pd.cut(morg_df.loc[:, "age"],
                                   bins=boundaries,
                                   labels=range(len(boundaries)-1),
                                   include_lowest=True, right=False)

morg_df
# Task 8

boundaries = range(0, 99, 10)
morg_df.loc[:, "hwpw_bin"] = pd.cut(morg_df.loc[:, "hours_worked_per_week"],
                                    bins=boundaries,
                                    labels=range(len(boundaries)-1),
                                    include_lowest=True, right=True)
morg_df
print("Morg columns types after Task 8")
print(morg_df.dtypes)
# Tasks 9-13
ft_filter = (morg_df["hours_worked_per_week"] >= 35)
ft = morg_df[ft_filter]
ft

morg_df
not_working_filter = (morg_df["employment_status"] != "Working")
not_working = morg_df[not_working_filter]
not_working
ft_1k_filter = ((morg_df["hours_worked_per_week"] >= 35) |
                (morg_df["earnings_per_week"] > 1000))
ft_1k = morg_df[ft_1k_filter]
ft_1k
# Task 12
race_value_cnts = morg_df.loc[:, "race"].value_counts()[:5]
race_value_cnts
race_gb = morg_df.groupby("race").size()
race_gb
# Task 14

students = pd.read_csv("data/students.csv")
grades = pd.read_csv("data/grades.csv")
extended_grades = pd.read_csv("data/extended_grades.csv")
students
grades
extended_grades
df = pd.merge(students, extended_grades, on="UCID", how="inner")
df0 = df.groupby(["Grade", "Major"]).size().reset_index()
df0
df0.rename(columns={0: "Count"}, inplace=True)
df0
