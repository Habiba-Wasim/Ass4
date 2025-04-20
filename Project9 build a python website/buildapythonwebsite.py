# # Project 9 Build A Python Website In 15 Minutes With Streamlit

# import streamlit as st
# import pandas as pd
# import random

# st.set_page_config(page_title="Student Data Generator", layout="wide")
# st.title("Student CSV File Generator")

# names = ["Ali", "Fahad", "Taha", "Ahmed", "Sara", "Bilal", "Aisha", "Faisal", "Hassan", "Hina", "Nida", "Hamza", "Zainab", "Habiba", "Iqra", "Bisma", "Laiba"]

# students = []
# for i in range(1, 16):
#     student = {
#         "Name": random.choice(names),
#         "Age": random.randint(18, 25),
#         "Grade": random.choice(["A", "B", "C", "D", "F"]),
#         "Marks": random.randint(40, 100),
#     }
#     students.append(student)
    
# df = pd.DataFrame(students)
# st.subheader("Generated Student Data")
# st.dataframe(df)

# csv_file = df.to_csv(index=False).encode("utf-8")
# csv_file= df.to_csv("Download CSV File", csv_file, "students.csv", "text/csv")
# st.success("Student Record Generated Successfully!")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
# Project 9 Build A Python Website In 15 Minutes With Streamlit

import streamlit as st
import pandas as pd
import random

# Page Config
st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("📚 Student CSV File Generator")

# Names for Random Generation
names = ["Ali", "Fahad", "Taha", "Ahmed", "Sara", "Bilal", "Aisha", "Faisal", "Hassan", "Hina", "Nida", "Hamza", "Zainab", "Habiba", "Iqra", "Bisma", "Laiba"]

# Generate Student Data
students = []
for i in range(1, 16):
    student = {
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "F"]),
        "Marks": random.randint(40, 100),
    }
    students.append(student)

# Create DataFrame
df = pd.DataFrame(students)

# Show Data
st.subheader("📊 Generated Student Data")
st.dataframe(df)

# Convert DataFrame to CSV
csv_data = df.to_csv(index=False).encode("utf-8")

# Add Download Button
st.download_button(
    label="📥 Download CSV File",
    data=csv_data,
    file_name="students.csv",
    mime="text/csv"
)

st.success("✅ Student Record Generated Successfully!")
    