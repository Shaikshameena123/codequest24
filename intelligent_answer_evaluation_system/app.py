import streamlit as st
import plotly.express as px
import os
from utils import (
    check_similarity,
    plagiarism_check,
    grammar_check,
    highlight_plagiarism,
)

st.set_page_config(page_title="Intelligent Answer Evaluation System", page_icon="📝", layout="wide")

# Dark/Light Mode Toggle
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

st.sidebar.button("Toggle Dark/Light Mode", on_click=toggle_dark_mode)

# CSS for Dark Mode
if st.session_state.dark_mode:
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #2E2E2E;
                color: white;
            }
            .stTextInput, .stTextArea {
                background-color: #1E1E1E;
                color: white;
                border: 1px solid #444;
            }
            .stButton {
                background-color: #007BFF;
                color: white;
            }
            h1, h2, h3, h4 {
                color: #FFD700;
            }
            .feedback {
                background-color: #F0F0F0;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #C0C0C0;
                color: #333;
                margin-top: 20px;
                font-weight: bold;
            }
        </style>
        """, unsafe_allow_html=True
    )

def load_model_answer():
    with open(os.path.join('data', 'model_answers.txt'), 'r') as file:
        return file.read().split("\n\n")[0]

def load_sample_student_answer(file_name):
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, 'data')
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, 'r') as file:
        return file.read()

if 'student_answer' not in st.session_state:
    st.session_state.student_answer = ""

uploaded_file = st.file_uploader("Upload Student Answer Script (txt only)", type=['txt'])

sample_answer_files = ["sample_student_answer1.txt", "sample_student_answer2.txt"]
sample_answer_choice = st.selectbox("Or choose a sample answer for testing:", sample_answer_files)

if uploaded_file:
    st.session_state.student_answer = uploaded_file.read().decode("utf-8")
else:
    st.session_state.student_answer = load_sample_student_answer(sample_answer_choice)

model_answer = load_model_answer()
st.markdown("<h1 style='text-align: center;'>📝 Intelligent Answer Evaluation System</h1>", unsafe_allow_html=True)

st.text_area("Model Answer", model_answer, height=150)
st.text_area("Student Answer", st.session_state.student_answer, height=150)

if st.button("Evaluate Answer"):
    similarity_score = check_similarity(st.session_state.student_answer, model_answer)
    reference_corpus = [model_answer]
    plagiarism_score = plagiarism_check(st.session_state.student_answer, reference_corpus)
    grammar_issues = grammar_check(st.session_state.student_answer)

    highlighted_text = highlight_plagiarism(st.session_state.student_answer, reference_corpus)
    st.markdown(f"**Highlighted Plagiarism:**\n\n{highlighted_text}", unsafe_allow_html=True)

    # Display Evaluation Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Answer Similarity", f"{similarity_score * 100:.2f}%", "Accuracy")
    col2.metric("Plagiarism Score", f"{plagiarism_score:.2f}%", "Originality")
    col3.metric("Grammar Issues", f"{len(grammar_issues)} issues", "Language Quality")

    # Feedback Generation
    feedback = []
    if similarity_score < 0.5:
        feedback.append("🔍 Consider revising your answer.")
    if plagiarism_score > 20:
        feedback.append("🚫 High similarity with other works detected.")
    if len(grammar_issues) > 5:
        feedback.append("📝 Review grammar errors for clarity.")

    # Animated Progress Bars and Icons
    st.balloons()  # Celebrate successful evaluation
    st.success("🎉 Congratulations! Your evaluation is complete.")  # Display success message

    # Styled Feedback Section
    st.markdown("<h4 style='color: #E56E00;'>Feedback</h4>", unsafe_allow_html=True)
    if feedback:
        feedback_message = "<br>".join(feedback)
        st.markdown(f"<div class='feedback'>{feedback_message}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='feedback'>✅ Great job! Your answer is well-structured and original.</div>", unsafe_allow_html=True)

    # Interactive Bar Chart for Progress Visualization
    categories = ['Similarity', 'Plagiarism', 'Grammar']
    values = [similarity_score * 100, 100 - plagiarism_score, 100 - len(grammar_issues)]
    fig = px.bar(x=categories, y=values, title="Evaluation Metrics", color=categories)
    st.plotly_chart(fig)

    # Color-Coded Feedback Sections
    st.markdown("<h4 style='color: green;'>Evaluation Summary</h4>", unsafe_allow_html=True)
    st.write(f"**Similarity:** {similarity_score * 100:.2f}%")
    st.write(f"**Plagiarism:** {plagiarism_score:.2f}%")
    st.write(f"**Grammar Issues:** {len(grammar_issues)}")

