#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
import streamlit as st
from PIL import Image
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
# Function to calculate weighted marks
def calculate_weighted_marks(obtained_marks, total_marks, weightage_per_item):
    return sum(
        (obtained / total) * weightage_per_item if total > 0 else 0
        for obtained, total in zip(obtained_marks, total_marks))
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
# Function to determine grade and GPA
def get_grade_and_gpa(marks):
    grading_criteria = [
        (85, "A", 4.00),
        (80, "A-", 3.66),
        (75, "B+", 3.33),
        (71, "B", 3.00),
        (68, "B-", 2.66),
        (64, "C+", 2.33),
        (61, "C", 2.00),
        (58, "C-", 1.66),
        (54, "D+", 1.30),
        (50, "D", 1.00),
        (0, "F", 0.00),]
    for threshold, grade, gpa in grading_criteria:
        if marks >= threshold:
            return grade, gpa
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
# Streamlit App: Theory Subject Page
def theory_subject_page():
    st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(to right, #f7f9fc, #eef2f7); /* Softer gradient */
        color: #333333;}
    .stButton>button {
        background-color: #f1f1f1;  /* Light Grey for Buttons */
        color: #333333;  /* Dark Text for Visibility */
        border-radius: 12px;
        padding: 10px;
        font-size: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;}
    .stButton>button:hover {
        background-color: #e0e0e0;  /* Slightly Darker Light Grey */
        transform: scale(1.05);  /* Slight zoom effect */}
    .stMarkdown>p {
        text-align: justify;
        color: #333;
        font-size: 16px;}
    .sidebar .sidebar-content {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);}
    .stHeader>h1 {
        color: #eab676;  /* Soft Beige */
        font-weight: bold;
        font-size: 30px;
        text-align: center;}
    .stSubheader>h2 {
        font-size: 22px;
        color: #388e3c;  /* Soft Green */}
    .card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;}
    .results {
        transition: background-color 0.3s ease;}
    .results:hover {
        background-color: #fff3e0; /* Soft light beige */}
    .stMarkdown ul {
        list-style-type: none;
        padding-left: 0;}
    .stMarkdown li {
        padding: 5px 0;}
    .stTextInput>label {
        font-size: 16px;
        color: #eab676; /* Soft Beige */}
    .stIcon {
        color: black !important;  /* Set all icons color to black */}
    </style>
    """, unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    st.sidebar.image("logo.png", use_container_width=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#    
    st.sidebar.title("CUI Marks Calculator:")
    st.sidebar.markdown(
    """
    <style>
    .justified-text {
        text-align: justify;}
    </style>
    <div class="justified-text">
        This dashboard calculates internal marks of Comsats University Islamabad. This is just for an idea.
    </div>
    """,
    unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    st.sidebar.title("About me:")
    st.sidebar.markdown(
        """
        - **Name:** Muhammad Faizan Akram  
        - **Reg No:** FA23-BBD-090  
        - **Email:** mfakram28@gmail.com
        """)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Session State Initialization
    if "quizzes" not in st.session_state:
        st.session_state.quizzes = [{"obtained": None, "total": None}]
    if "assignments" not in st.session_state:
        st.session_state.assignments = [{"obtained": None, "total": None}]
    if "internal_marks" not in st.session_state:
        st.session_state.internal_marks = None
    if "predicted_marks" not in st.session_state:
        st.session_state.predicted_marks = None
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Quiz Section
    st.header("📚 Quizzes")
    quiz_obtained = []
    quiz_total = []
    quiz_cols = st.columns(2)
    for i, quiz in enumerate(st.session_state.quizzes):
        with quiz_cols[0]:
            obtained = st.number_input(
                f"Quiz {i + 1} Obtained Marks:",
                min_value=0.0,
                step=0.1,
                key=f"quiz_obtained_{i}",
                value=quiz["obtained"],
                format="%.1f",
                help="Enter the marks you scored in this quiz.")
        with quiz_cols[1]:
            total = st.number_input(
                f"Quiz {i + 1} Total Marks:",
                min_value=0.0,
                step=0.1,
                key=f"quiz_total_{i}",
                value=quiz["total"],
                format="%.1f",
                help="Enter the maximum marks for this quiz.")
    # Add New Quiz Button with Icon
    if st.button("➕ Add Quiz"):
        st.session_state.quizzes.append({"obtained": None, "total": None})
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Assignment Section
    st.header("📝 Assignments")
    assignment_obtained = []
    assignment_total = []
    assignment_cols = st.columns(2)
    for i, assignment in enumerate(st.session_state.assignments):
        with assignment_cols[0]:
            obtained = st.number_input(
                f"Assignment {i + 1} Obtained Marks:",
                min_value=0.0,
                step=0.1,
                key=f"assignment_obtained_{i}",
                value=assignment["obtained"],
                format="%.1f",
                help="Enter the marks you received for this assignment.")
        with assignment_cols[1]:
            total = st.number_input(
                f"Assignment {i + 1} Total Marks:",
                min_value=0.0,
                step=0.1,
                key=f"assignment_total_{i}",
                value=assignment["total"],
                format="%.1f",
                help="Enter the maximum marks for this assignment.")
        assignment_obtained.append(obtained)
        assignment_total.append(total)

    # Add New Assignment Button with Icon
    if st.button("➕ Add Assignment"):
        st.session_state.assignments.append({"obtained": None, "total": None})
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Mid-Term Section
    st.header("📊 Mid-Term")
    midterm_cols = st.columns(2)
    with midterm_cols[0]:
        midterm_obtained = st.number_input(
            "Obtained Marks for Mid-Term:",
            min_value=0.0,
            step=0.1,
            value=None,
            format="%.1f",
            help="Enter the marks you received for the mid-term exam.")
    with midterm_cols[1]:
        midterm_total = st.number_input(
            "Total Marks for Mid-Term:",
            min_value=0.0,
            step=0.1,
            value=None,
            format="%.1f",
            help="Enter the maximum possible marks for the mid-term.")
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Weightage Variables
    quiz_weightage = 15
    assignment_weightage = 10
    midterm_weightage = 25
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Initialization of marks variables
    quiz_marks = 0
    assignment_marks = 0
    midterm_marks = 0
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Calculation Button with Icon
    if st.button("📈 Calculate Internal Marks"):
        quiz_weightage_per_item = (
            quiz_weightage / len(st.session_state.quizzes)
            if st.session_state.quizzes
            else 0)
        assignment_weightage_per_item = (
            assignment_weightage / len(st.session_state.assignments)
            if st.session_state.assignments
            else 0)

        quiz_marks = calculate_weighted_marks(
            quiz_obtained, quiz_total, quiz_weightage_per_item)
        assignment_marks = calculate_weighted_marks(
            assignment_obtained, assignment_total, assignment_weightage_per_item)
        midterm_marks = (
            (midterm_obtained / midterm_total) * midterm_weightage
            if midterm_total > 0
            else 0)

        st.session_state.internal_marks = quiz_marks + assignment_marks + midterm_marks
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Display Results Section with Hover Effect
    if st.session_state.internal_marks is not None:
        st.subheader("📈 Results")
        st.markdown('<div class="results card">', unsafe_allow_html=True)
        st.write(f"**Total Quiz Marks:** {quiz_marks:.1f} / {quiz_weightage}")
        st.write(
            f"**Total Assignment Marks:** {assignment_marks:.1f} / {assignment_weightage}")
        st.write(f"**Total Mid-Term Marks:** {midterm_marks:.1f} / {midterm_weightage}")
        st.write(f"**Total Internal Marks:** {st.session_state.internal_marks:.1f} / 50")
        st.markdown('</div>', unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
# Streamlit App: Lab Subject Page
def lab_subject_page():
    st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background: linear-gradient(to right, #f7f9fc, #eef2f7); /* Softer gradient */
        color: #333333;}
    .stButton>button {
        background-color: #f1f1f1;  /* Light Grey for Buttons */
        color: #333333;  /* Dark Text for Visibility */
        border-radius: 12px;
        padding: 10px;
        font-size: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;}
    .stButton>button:hover {
        background-color: #e0e0e0;  /* Slightly Darker Light Grey */
        transform: scale(1.05);  /* Slight zoom effect */}
    .stMarkdown>p {
        text-align: justify;
        color: #333;
        font-size: 16px;}
    .sidebar .sidebar-content {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);}
    .stHeader>h1 {
        color: #eab676;  /* Soft Beige */
        font-weight: bold;
        font-size: 30px;
        text-align: center;}
    .stSubheader>h2 {
        font-size: 22px;
        color: #388e3c;  /* Soft Green */}
    .card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;}
    .results {
        transition: background-color 0.3s ease;}
    .results:hover {
        background-color: #fff3e0; /* Soft light beige */}
    .stMarkdown ul {
        list-style-type: none;
        padding-left: 0;}
    .stMarkdown li {
        padding: 5px 0;}
    .stTextInput>label {
        font-size: 16px;
        color: #eab676; /* Soft Beige */}
    .stIcon {
        color: black !important;  /* Set all icons color to black */}
    </style>
    """, unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    st.sidebar.image("logo.png", use_container_width=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#    
    st.sidebar.title("CUI Marks Calculator:")
    st.sidebar.markdown(
    """
    <style>
    .justified-text {
        text-align: justify;}
    </style>
    <div class="justified-text">
        This dashboard calculates internal marks of Comsats University Islamabad. This is just for an idea.
    </div>
    """,
    unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    st.sidebar.title("About me:")
    st.sidebar.markdown(
        """
        - **Name:** Muhammad Faizan Akram  
        - **Reg No:** FA23-BBD-090  
        - **Email:** mfakram28@gmail.com
        """)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#    
    # Session State Initialization
    if "quizzes" not in st.session_state:
        st.session_state.quizzes = [{"obtained": None, "total": None}]
    if "assignments" not in st.session_state:
        st.session_state.assignments = [{"obtained": None, "total": None}]
    if "lab_assignments" not in st.session_state:
        st.session_state.lab_assignments = [{"obtained": None, "total": None}]
    if "lab_midterm" not in st.session_state:
        st.session_state.lab_midterm = {"obtained": None, "total": None}
    if "midterm" not in st.session_state:
        st.session_state.midterm = {"obtained": None, "total": None}
    if "internal_marks" not in st.session_state:
        st.session_state.internal_marks = None
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
# Quizzes Section
    st.header("📚 Quizzes")
    quiz_obtained = []
    quiz_total = []
    quiz_cols = st.columns(2)
    for i, quiz in enumerate(st.session_state.quizzes):
        with quiz_cols[0]:
            obtained = st.number_input(
                f"Quiz {i + 1} Obtained Marks:",
                min_value=0.0,
                step=0.1,
                key=f"quiz_obtained_{i}",
                value=quiz["obtained"],
                format="%.1f",
                help="Enter the marks you scored in this quiz.")
        with quiz_cols[1]:
            total = st.number_input(
                f"Quiz {i + 1} Total Marks:",
                min_value=0.0,
                step=0.1,
                key=f"quiz_total_{i}",
                value=quiz["total"],
                format="%.1f",
                help="Enter the maximum marks for this quiz.")
    quiz_obtained.append(obtained)
    quiz_total.append(total)

    if st.button("➕ Add Quiz"):
        st.session_state.quizzes.append({"obtained": None, "total": None})
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Assignment Section
    st.header("📝 Assignments")
    assignment_obtained = []
    assignment_total = []
    assignment_cols = st.columns(2)
    for i, assignment in enumerate(st.session_state.assignments):
        with assignment_cols[0]:
            obtained = st.number_input(
                f"Assignment {i + 1} Obtained Marks:",
                min_value=0.0,
                step=0.1,
                key=f"assignment_obtained_{i}",
                value=assignment["obtained"],
                format="%.1f",
                help="Enter the marks you received for this assignment.")
        with assignment_cols[1]:
            total = st.number_input(
                f"Assignment {i + 1} Total Marks:",
                min_value=0.0,
                step=0.1,
                key=f"assignment_total_{i}",
                value=assignment["total"],
                format="%.1f",
                help="Enter the maximum marks for this assignment.")
        assignment_obtained.append(obtained)
        assignment_total.append(total)

    # Add New Assignment Button with Icon
    if st.button("➕ Add Assignment"):
        st.session_state.assignments.append({"obtained": None, "total": None})
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    st.header("💻 Lab Assignments")
    lab_obtained = []
    lab_total = []
    lab_cols = st.columns(2)
    for i, lab in enumerate(st.session_state.lab_assignments):
        with lab_cols[0]:
            obtained = st.number_input(
                f"Lab Assignment {i + 1} Obtained Marks:",
                min_value=0.0,
                step=0.1,
                key=f"lab_obtained_{i}",
                value=lab["obtained"],
                format="%.1f",
                help="Enter marks obtained in this lab assignment.")
        with lab_cols[1]:
            total = st.number_input(
                f"Lab Assignment {i + 1} Total Marks:",
                min_value=0.0,
                step=0.1,
                key=f"lab_total_{i}",
                value=lab["total"],
                format="%.1f",
                help="Enter total marks for this lab assignment.")
        lab_obtained.append(obtained)
        lab_total.append(total)

    if st.button("➕ Add Lab Assignment"):
        st.session_state.lab_assignments.append({"obtained": None, "total": None})
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    st.header("💻 Lab Mid-Term")
    lab_midterm_cols = st.columns(2)
    with lab_midterm_cols[0]:
        lab_midterm_obtained = st.number_input(
            "Obtained Marks for Lab Mid-Term:",
            min_value=0.0,
            step=0.1,
            value=st.session_state.lab_midterm["obtained"],
            format="%.1f",
            help="Enter marks obtained in lab mid-term.")
    with lab_midterm_cols[1]:
        lab_midterm_total = st.number_input(
            "Total Marks for Lab Mid-Term:",
            min_value=0.0,
            step=0.1,
            value=st.session_state.lab_midterm["total"],
            format="%.1f",
            help="Enter total marks for lab mid-term.")
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    st.header("📊 Mid-Term")
    midterm_cols = st.columns(2)
    with midterm_cols[0]:
        midterm_obtained = st.number_input(
            "Obtained Marks for Mid-Term:",
            min_value=0.0,
            step=0.1,
            value=st.session_state.midterm["obtained"],
            format="%.1f",
            help="Enter the marks you received for the mid-term exam.")
    with midterm_cols[1]:
        midterm_total = st.number_input(
            "Total Marks for Mid-Term:",
            min_value=0.0,
            step=0.1,
            value=st.session_state.midterm["total"],
            format="%.1f",
            help="Enter the maximum possible marks for the mid-term.")
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Weightage Variables
    quiz_weightage = 15
    assignment_weightage = 10
    midterm_weightage = 25
    lab_assignment_weightage = 25
    lab_midterm_weightage = 25
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Initialization of marks variables
    quiz_marks = 0
    assignment_marks = 0
    lab_assignment_marks = 0
    lab_midterm_marks = 0
    midterm_marks = 0
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
 # Calculate Internal Marks
    if st.button("📈 Calculate Internal Marks"):
        quiz_weightage_per_item = (
            quiz_weightage / len(st.session_state.quizzes)
            if st.session_state.quizzes
            else 0)
        assignment_weightage_per_item = (
            assignment_weightage / len(st.session_state.assignments)
            if st.session_state.assignments
            else 0)
        lab_assingnment_weightage_per_item = (
            lab_assignment_weightage / len(st.session_state.lab_assignments)
            if st.session_state.lab_assignments
            else 0)

        quiz_marks = calculate_weighted_marks(
            quiz_obtained, quiz_total, quiz_weightage_per_item)
        assignment_marks = calculate_weighted_marks(
            assignment_obtained, assignment_total, assignment_weightage_per_item)
        lab_assignment_marks = calculate_weighted_marks(
            lab_obtained, lab_total, lab_assingnment_weightage_per_item)
        lab_midterm_marks = (
            (lab_midterm_obtained / lab_midterm_total) * lab_midterm_weightage 
            if lab_midterm_total > 0 
            else 0)
        midterm_marks = (
            (midterm_obtained / midterm_total) * midterm_weightage
            if midterm_total > 0
            else 0)
        st.session_state.internal_marks = (((quiz_marks) + (assignment_marks) + (midterm_marks)) * 0.75) + (((lab_assignment_marks) + (lab_midterm_marks)) * 0.25)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Display Results Section with Hover Effect
    if st.session_state.internal_marks is not None:
        st.subheader("📈 Results")
        st.markdown('<div class="results card">', unsafe_allow_html=True)
        st.write(f"**Total Quiz Marks:** {quiz_marks:.1f}")
        st.write(f"**Total Assignment Marks:** {assignment_marks:.1f}")
        st.write(f"**Total Lab Assignment Marks:** {lab_assignment_marks:.1f}")
        st.write(f"**Total Lab Mid-Term Marks:** {lab_midterm_marks:.1f}")
        st.write(f"**Total Mid-Term Marks:** {midterm_marks:.1f}")
        st.write(f"**Total Internal Marks:** {st.session_state.internal_marks:.1f}")
        st.markdown('</div>', unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
# Main Function
def main():
    st.set_page_config(
        page_title="Internal Marks Calculator",
        layout="wide",
        initial_sidebar_state="expanded",)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
     # Main Section with Title and Buttons
    st.markdown(
    """
    <h1 style="text-align: center; color: #333333; font-weight: bold; font-size: 50px;">
        CUI Internal Marks Calculator
    </h1>
    """,
    unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
    # Navigation Below Title with Updated Text Size
    st.markdown(
        """
        <h2 style="text-align: left; color: #333333; font-size: 24px;">
            🔍 Subject Nature:
        </h2>
        """,
        unsafe_allow_html=True)

    # Navigation Below Title
    page = st.radio("Select:", ["📝 Theory Subject", "💻 Lab Subject"], horizontal=True)

    if page == "📝 Theory Subject":
        theory_subject_page()
    elif page == "💻 Lab Subject":
        lab_subject_page()



if __name__ == "__main__":
    main()
#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#