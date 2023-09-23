# Sentiment Analysis Project
This project involves sentiment analysis of textual data to determine the polarity and subjectivity of the content. The analysis is performed on a given text using natural language processing (NLP) techniques.

## Features

## Sentiment Analysis

**Positive Score:** Assigns a value of +1 for each positive word found in the text and calculates the total positive score.
**Negative Score:** Assigns a value of -1 for each negative word found in the text and calculates the total negative score (multiplied by -1 to ensure a positive score).
**Polarity Score:** Determines the overall polarity of the text using the formula: (Positive Score - Negative Score) / ((Positive Score + Negative Score) + 0.000001).
**Subjectivity Score:** Measures the subjectivity of the text using the formula: (Positive Score + Negative Score) / (Total Words after cleaning + 0.000001).

## Readability Analysis

**Average Sentence Length:** Calculates the average number of words per sentence in the text.
**Percentage of Complex Words:** Calculates the percentage of words with more than two syllables.
**Fog Index:** Computes the Fog Index using the formula: 0.4 * (Average Sentence Length + Percentage of Complex Words).
**Average Number of Words Per Sentence:** Calculates the average number of words per sentence.

## Additional Metrics

**Word Count:** Counts the total number of cleaned words in the text after removing stopwords and punctuation.
**Syllable Count Per Word:** Determines the number of syllables in each word, considering exceptions like words ending with "es" or "ed".
**Personal Pronouns**: Counts the occurrences of personal pronouns (e.g., I, we, my, ours, us) in the text.
**Average Word Length:** Calculates the average length of words in the text.

## Usage

Input Text:
The tool accepts text input or allows users to upload a text file for analysis.

Output:
The tool displays the sentiment analysis and readability metrics for the provided text.

## Setup
To run the sentiment analysis tool:

```
Clone the repository:
git clone https://github.com/yourusername/sentiment_analysis.git

Change to the project directory:
cd sentiment_analysis

Install the required dependencies:
pip install -r requirements.txt
```

Launch the tool:
```
streamlit run main.py
```
Access the tool at http://localhost:8501 in your web browser.

## Note:

Ensure that the provided text adheres to the required format for accurate analysis.
The tool offers flexibility for customization or extension based on specific needs.
