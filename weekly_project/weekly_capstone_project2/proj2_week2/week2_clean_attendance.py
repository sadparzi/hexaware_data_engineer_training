"""
Employee Attendance & Productivity Tracker - Week 2
Attendance & Task Data Cleanup Using Python (Pandas, NumPy)
"""

import pandas as pd
import numpy as np

# ============================================================
# Load Data
# ============================================================

df = pd.read_csv('attendance.csv')

print("=== Raw Data Info ===")
print(df.info())
print()
print("=== Raw Data Preview ===")
print(df.head(10))
print()
print("=== Missing Values per Column ===")
print(df.isnull().sum())
print()

# ============================================================
# Clean Missing / Invalid Entries
# ============================================================

# clock_in / clock_out: missing means Absent or incomplete log -> leave as NaT,
# work_hours will naturally be NaN for these (handled below)
df['clock_in'] = pd.to_datetime(df['clock_in'], format='%H:%M', errors='coerce')
df['clock_out'] = pd.to_datetime(df['clock_out'], format='%H:%M', errors='coerce')

# tasks_completed: missing -> assume 0 (no tasks logged)
df['tasks_completed'] = df['tasks_completed'].fillna(0)

# Ensure status is consistent: if clock_in is missing and status wasn't marked Absent, correct it
df.loc[df['clock_in'].isna() & (df['status'] != 'Absent'), 'status'] = 'Absent'

# ============================================================
# Correct Data Types
# ============================================================

df['work_date'] = pd.to_datetime(df['work_date'])
df['employee_id'] = df['employee_id'].astype(int)
df['tasks_completed'] = df['tasks_completed'].astype(int)
df['tasks_assigned'] = df['tasks_assigned'].astype(int)

# ============================================================
# Calculate Work Hours, Break Time, Productivity Score (NumPy)
# ============================================================

# work_hours: hours between clock_in and clock_out
df['work_hours'] = (df['clock_out'] - df['clock_in']).dt.total_seconds() / 3600
df['work_hours'] = np.round(df['work_hours'], 2)

# Standard workday assumed as 9 hours -> break_time = work_hours - 9 hrs of "core" work
# (anything beyond 9 hours of presence assumed as break/buffer, floored at 0)
STANDARD_DAY_HOURS = 9
df['break_time_hrs'] = np.where(
    df['work_hours'].notna(),
    np.clip(df['work_hours'] - STANDARD_DAY_HOURS, 0, None),
    np.nan
)
df['break_time_hrs'] = np.round(df['break_time_hrs'], 2)

# Late login flag: clock_in after 09:15
df['late_login'] = df['clock_in'].dt.time > pd.to_datetime('09:15', format='%H:%M').time()
df['late_login'] = df['late_login'].fillna(False)

# productivity_score: tasks completed per hour worked (NaN-safe, avoid div by 0)
df['productivity_score'] = np.where(
    (df['work_hours'].notna()) & (df['work_hours'] > 0),
    np.round(df['tasks_completed'] / df['work_hours'], 2),
    0
)

print("=== Cleaned Data with Calculated Fields ===")
print(df.head(10))
print()

# ============================================================
# Top Performers (highest avg productivity score)
# ============================================================

performance_summary = df.groupby(['employee_id', 'employee_name', 'department']).agg(
    avg_work_hours=('work_hours', 'mean'),
    avg_productivity_score=('productivity_score', 'mean'),
    total_tasks_completed=('tasks_completed', 'sum'),
    days_present=('status', lambda x: (x == 'Present').sum()),
    days_absent=('status', lambda x: (x == 'Absent').sum()),
    late_logins=('late_login', 'sum')
).reset_index()

performance_summary['avg_work_hours'] = performance_summary['avg_work_hours'].round(2)
performance_summary['avg_productivity_score'] = performance_summary['avg_productivity_score'].round(2)

top_performers = performance_summary.sort_values('avg_productivity_score', ascending=False).head(3)
bottom_performers = performance_summary.sort_values('avg_productivity_score', ascending=True).head(3)

print("=== Top 3 Performers ===")
print(top_performers)
print()
print("=== Bottom 3 Performers ===")
print(bottom_performers)
print()

# ============================================================
# Frequent Absentees
# ============================================================

frequent_absentees = performance_summary.sort_values('days_absent', ascending=False)
frequent_absentees = frequent_absentees[frequent_absentees['days_absent'] > 0]

print("=== Frequent Absentees ===")
print(frequent_absentees[['employee_name', 'department', 'days_absent', 'late_logins']])
print()

# ============================================================
# Department-Level Summary
# ============================================================

dept_summary = df.groupby('department').agg(
    avg_work_hours=('work_hours', 'mean'),
    avg_productivity_score=('productivity_score', 'mean'),
    total_absences=('status', lambda x: (x == 'Absent').sum())
).round(2).reset_index()

print("=== Department-Level Summary ===")
print(dept_summary)
print()

# ============================================================
# Save Cleaned Dataset
# ============================================================

df.to_csv('attendance_cleaned.csv', index=False)
performance_summary.to_csv('employee_performance_summary.csv', index=False)

print("Cleaned dataset saved as attendance_cleaned.csv")
print("Performance summary saved as employee_performance_summary.csv")
