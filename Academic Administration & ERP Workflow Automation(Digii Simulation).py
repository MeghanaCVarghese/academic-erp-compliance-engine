#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


# Generate Mock Student Data mimicking a University Registry
np.random.seed(42)
data = {
    'Student_ID': [f"VU2026_{100+i}" for i in range(50)],
    'Student_Name': [f"Student_{i+1}" for i in range(50)],
    'Department': np.random.choice(['Computer Science', 'Data Science', 'Business Analytics', 'Commerce'], 50),
    'Attendance_Percentage': np.random.randint(60, 100, 50),
    'Fees_Pending_INR': np.random.choice([0, 0, 0, 15000, 25000, 0], 50), # Most have cleared fees
    'Submission_Status': np.random.choice(['Complete', 'Complete', 'Pending Docs'], 50)
}

df = pd.DataFrame(data)
# Save the raw data as a mock database file
df.to_csv('Vidyashilp_Raw_Student_Records.csv', index=False)
print("Mock University Database Generated Successfully!")


# In[5]:


# Load the raw student records
student_df = pd.read_csv('Vidyashilp_Raw_Student_Records.csv')

# 2. Executive Assistant Logic Engine (Replicating Digii Modules)
def process_exam_eligibility(row):
    # Rule 1: Attendance must be >= 75%
    # Rule 2: Fees pending must be 0
    # Rule 3: Registration documentation must be complete
    
    reasons = []
    if row['Attendance_Percentage'] < 75:
        reasons.append("Low Attendance (<75%)")
    if row['Fees_Pending_INR'] > 0:
        reasons.append(f"Pending Dues (₹{row['Fees_Pending_INR']})")
    if row['Submission_Status'] == 'Pending Docs':
        reasons.append("Missing Academic Documents")
        
    if len(reasons) == 0:
        return "ELIGIBLE", "None"
    else:
        return "DETAINED", " & ".join(reasons)

# Apply the administrative policy logic
student_df[['Exam_Eligibility_Status', 'Reason_For_Detention']] = student_df.apply(
    lambda r: pd.Series(process_exam_eligibility(r)), axis=1
)

# 3. Generate Executive Summary Reports for the Registrar
total_students = len(student_df)
eligible_count = len(student_df[student_df['Exam_Eligibility_Status'] == 'ELIGIBLE'])
detained_count = total_students - eligible_count

print("--- REGISTRAR'S OFFICE COMPLIANCE REPORT ---")
print(f"Total Enrolled Students: {total_students}")
print(f"Approved for Hall Tickets: {eligible_count} ({(eligible_count/total_students)*100:.1f}%)")
print(f"Flagged / Detained Students: {detained_count} ({(detained_count/total_students)*100:.1f}%)")
print("--------------------------------------------")

# Export separate, clean actionable files for the department heads
detained_list = student_df[student_df['Exam_Eligibility_Status'] == 'DETAINED']
detained_list.to_csv('Actionable_Detained_Students_Report.csv', index=False)

eligible_list = student_df[student_df['Exam_Eligibility_Status'] == 'ELIGIBLE']
eligible_list.to_csv('Final_Hall_Ticket_Generation_List.csv', index=False)

print("\nReports successfully exported as clean CSVs for institutional workflows!")


# In[ ]:




