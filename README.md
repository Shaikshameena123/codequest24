# Intelligent Answer Evaluation System 📝

This project aims to evaluate student answers against a model answer using various metrics, such as similarity, plagiarism detection, and grammar checks. The application is built using Streamlit and integrates pre-trained models and natural language processing (NLP) techniques for evaluation.
## Architecture Diagram

The overall architecture of the Intelligent Answer Evaluation System is as follows:

![WhatsApp Image 2024-10-19 at 01 34 20_bb22e7a0](https://github.com/user-attachments/assets/a3213d95-7c87-459d-b611-192baaa0a74c)


## Software Tools Used

1. **Streamlit**: Used for building the web application interface.
2. **Python**: Main programming language used for developing the project's backend.
3. **Sentence Transformers**: For embedding texts and computing sentence similarity.
4. **LanguageTool**: Used for grammar and spell checking.
5. **scikit-learn**: Provides machine learning tools such as cosine similarity.
6. **Plotly**: Used for creating interactive plots and visualizations.
7. **Regular Expressions**: Used for highlighting plagiarized text within the student's answer.
8. **Textstat**: Computes readability scores such as the Flesch Reading Ease score.
9. **GitHub**: Used for version control and collaborative development.

## Step-by-Step Procedure to Execute the Solution

### Step 1: Clone the repository

> git clone https://github.com/Shaikshameena123/codequest24.git
> 
> cd codequest24

### Use terminal to execute the following steps:

Step 2: Install required dependencies
Make sure Python is installed. Install the necessary dependencies using the requirements.txt file:

> pip install -r requirements.txt

Step 3: Prepare data
Ensure that the data folder contains the required student answer scripts and model answer files.

Step 4: Run the application
You can start the Streamlit application by running:

> streamlit run app.py

Step 5: Use the Application
' Upload a student answer script (in .txt format) or select a sample student answer.

. Click "Evaluate Answer" to check the similarity, plagiarism, and grammar issues.

. View the evaluation metrics, including answer similarity, plagiarism score, and grammar issues.

. Review the feedback and performance visualization.

Step 6: View the Results
The application will provide a summary of evaluation metrics and highlight plagiarized content. Grammar issues will also be displayed, with appropriate feedback for improvement.

Expected Output:

. Plagiarism score (as a percentage)

. Similarity score (as a percentage)

. Grammar issues with context

. Readability score for the student's answer



