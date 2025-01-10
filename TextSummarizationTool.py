#!/usr/bin/env python
# coding: utf-8
# Download NLTK data files (only need to run this once)
# nltk.download('punkt')
# nltk.download('stopwords')

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import heapq

def summarize_text(text, summary_ratio=0.4):
    """
    Summarize the input text using NLP techniques.

    Args:
        text (str): The text to summarize.
        summary_ratio (float): Proportion of sentences to retain in the summary.

    Returns:
        str: The summarized text.
    """
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize the text into words and remove stopwords
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Calculate word frequencies
    word_frequencies = Counter(filtered_words)
    max_frequency = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency

    # Score sentences based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]

    # Select the top sentences based on the summary ratio
    summary_length = int(len(sentences) * summary_ratio)
    summary_length = max(1, summary_length)  # Ensure at least one sentence
    summarized_sentences = heapq.nlargest(summary_length, sentence_scores, key=sentence_scores.get)

    # Combine the selected sentences into a summary
    summary = ' '.join(summarized_sentences)
    return summary

input_text = input("Enter the text to be summarized : ")
print("\nSummarized Text:\n", summarize_text(input_text))






