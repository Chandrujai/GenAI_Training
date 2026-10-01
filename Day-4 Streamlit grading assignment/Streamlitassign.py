import streamlit as st

st.title("Grade Calculator")

mark = st.number_input(
    "Enter a mark (0–100)",
    min_value=0,
    max_value=100,
    value=0,
    step=1,
)

if mark >= 90:
    grade = "A"
    st.success(f"You entered **{mark}**. Your grade is **{grade}**.")
elif mark >= 80:
    grade = "B"
    st.success(f"You entered **{mark}**. Your grade is **{grade}**.")
elif mark >= 70:
    grade = "C"
    st.info(f"You entered **{mark}**. Your grade is **{grade}**.")
elif mark >= 60:
    grade = "D"
    st.write(f"You entered **{mark}**. Your grade is **{grade}**.")
elif mark >= 35 and mark < 60:
    grade = "E"
    st.warning(f"You entered **{mark}**. Your grade is **{grade}**.")
else:
    grade = "F"
    st.error(f"You entered **{mark}**. Your grade is **{grade}**.")

