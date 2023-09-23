import nltk
nltk.download('punkt')

nltk.download('stopwords')

import nltk
nltk.download('cmudict')

import streamlit as st
import string
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Function to count syllables
def count_syllables(word):
    subtract_syllables = ["es", "ed", "e"]
    for ending in subtract_syllables:
        if word.endswith(ending):
            return max(1, count_vowels(word) - 1)
    return count_vowels(word)

# Function to count vowels
def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

# Function to determine if a word is complex
def is_complex_word(word):
    return count_syllables(word) > 2

# Function to perform sentiment analysis and readability
def analyze_sentiment_and_readability(text):
    lower_case = text.lower()
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    tokenized_words = word_tokenize(cleaned_text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in tokenized_words if word not in stop_words]

    with open('cleaned_positive_words.txt', 'r') as file:
        positive_words = set(file.read().splitlines())

    with open('cleaned_negative_words.txt', 'r', encoding='latin-1') as file:
        negative_words = set(file.read().splitlines())

    positive_score = sum(1 for word in filtered_words if word.lower() in positive_words)
    negative_score = sum(1 for word in filtered_words if word.lower() in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(filtered_words) + 0.000001)

    final_words = [word for word in filtered_words if word not in stop_words]
    complex_word_count = sum(1 for word in final_words if is_complex_word(word))

    word_count = len(final_words)
    syllable_count_per_word = [count_syllables(word) for word in final_words]

    personal_pronouns_count = sum(1 for word in tokenized_words if re.match(r'\b(?:i|we|my|ours|us)\b', word, re.IGNORECASE))

    total_characters = sum(len(word) for word in final_words)
    average_word_length = total_characters / word_count

    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    num_words = len(tokenized_words)
    average_sentence_length = num_words / num_sentences

    num_complex_words = sum(1 for word in filtered_words if len(nltk.corpus.cmudict.dict().get(word, [])) >= 3)
    percentage_complex_words = (num_complex_words / num_words) * 100
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
    average_words_per_sentence = num_words / num_sentences

    return {
        "positive_score": positive_score,
        "negative_score": negative_score,
        "polarity_score": polarity_score,
        "subjectivity_score": subjectivity_score,
        "average_sentence_length": average_sentence_length,
        "percentage_complex_words": percentage_complex_words,
        "fog_index": fog_index,
        "average_words_per_sentence": average_words_per_sentence,
        "complex_word_count": complex_word_count,
        "word_count": word_count,
        "syllable_count_per_word": syllable_count_per_word,
        "personal_pronouns_count": personal_pronouns_count,
        "average_word_length": average_word_length
    }

# Streamlit app
def main():
    st.title("Sentiment Analysis and Readability Tool")

    # User input
    option = st.radio("Choose an option:", ("Enter Text", "Upload Text File"))
    user_input = ""
    if option == "Enter Text":
        user_input = st.text_area("Input Text (100-150 words)", "Type here...")
    else:
        uploaded_file = st.file_uploader("Choose a text file...", type=["txt"])
        if uploaded_file is not None:
            uploaded_text = uploaded_file.read().decode("utf-8")
            user_input = st.text_area("Uploaded Text", uploaded_text, height=250)

    # Analyze button
    if st.button("Analyze"):
        # Perform sentiment analysis and readability analysis
        results = analyze_sentiment_and_readability(user_input)

        # Display analysis results
        st.header("Analysis Results")
        st.write("Sentiment Analysis:")
        st.write("Positive Score:", results["positive_score"])
        st.write("Negative Score:", results["negative_score"])
        st.write("Polarity Score:", results["polarity_score"])
        st.write("Subjectivity Score:", results["subjectivity_score"])

        st.write("\nAnalysis of Readability:")
        st.write("Average Sentence Length:", results["average_sentence_length"])
        st.write("Percentage of Complex Words:", results["percentage_complex_words"])
        st.write("Fog Index:", results["fog_index"])
        st.write("Average Number of Words Per Sentence:", results["average_words_per_sentence"])
        st.write("Complex Word Count:", results["complex_word_count"])
        st.write("Word Count:", results["word_count"])
        st.write("Syllable Count Per Word:", results["syllable_count_per_word"])
        st.write("Personal Pronouns Count:", results["personal_pronouns_count"])
        st.write("Average Word Length:", results["average_word_length"])

if __name__ == "__main__":
    main()


