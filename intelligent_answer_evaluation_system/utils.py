import language_tool_python
import re
from sentence_transformers import SentenceTransformer, util
import requests
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from spellchecker import SpellChecker
import textstat

plagiarism_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


def check_similarity(student_answer, model_answer):
    """Evaluate similarity between the student's answer and the model answer using cosine similarity."""
    vectorizer = TfidfVectorizer().fit_transform([student_answer, model_answer])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    return cosine_sim[0, 1]

def plagiarism_check(student_answer, reference_corpus):
    """Check for plagiarism using a pre-trained model (without using APIs)."""
    student_embedding = plagiarism_model.encode([student_answer], convert_to_tensor=True)
    max_similarity = 0

    for reference_answer in reference_corpus:
        reference_embedding = plagiarism_model.encode([reference_answer], convert_to_tensor=True)
        similarity = cosine_similarity([student_embedding.cpu().numpy()[0]], [reference_embedding.cpu().numpy()[0]])[0][0]
        max_similarity = max(max_similarity, similarity)

    return max_similarity * 100  # Return plagiarism similarity score in percentage


def grammar_check(student_answer):
    spell = SpellChecker()
    words = student_answer.split()
    
    # Check for misspelled words
    misspelled = spell.unknown(words)
    grammar_issues = [{'error': f"Misspelled word: {word}", 'context': word} for word in misspelled]

    # Calculate readability score (you may keep this)
    readability_score = textstat.flesch_reading_ease(student_answer)

    return grammar_issues, readability_score

def highlight_plagiarism(student_answer, reference_corpus):
    # Highlight plagiarized words
    highlighted_text = student_answer
    for word in reference_corpus[0].split():
        highlighted_text = re.sub(rf'\b{word}\b', f'<span style="color: red; font-weight: bold;">{word}</span>', highlighted_text)
    return highlighted_text
