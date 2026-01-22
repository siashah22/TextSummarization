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

# Ensure required NLTK resources are available
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, summary_ratio=0.4, language='english'):

    # Sentence tokenization
    sentences = sent_tokenize(text)

    # Early exit for very short text (efficiency optimization)
    if len(sentences) <= 2:
        return text

    # Word tokenization and preprocessing
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words(language))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Word frequency calculation
    word_frequencies = Counter(filtered_words)
    max_frequency = max(word_frequencies.values(), default=1)

    # Normalize word frequencies
    for word in word_frequencies:
        word_frequencies[word] /= max_frequency

    # Sentence scoring with length normalization
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        for word in sentence_words:
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

        # Normalize by sentence length to avoid bias
        if sentence in sentence_scores:
            sentence_scores[sentence] /= len(sentence_words)

    # Determine summary length
    summary_length = max(1, int(len(sentences) * summary_ratio))

    # Efficient Top-K sentence selection
    summarized_sentences = heapq.nlargest(summary_length, sentence_scores, key=sentence_scores.get)

    # Preserve original sentence order
    summarized_sentences = sorted(summarized_sentences, key=lambda s: sentences.index(s))

    # Generate final summary
    summary = ' '.join(summarized_sentences)
    return summary


if __name__ == "__main__":
    input_text = input("Enter the text to be summarized:\n")
    print("\nSummarized Text:\n")
    print(summarize_text(input_text))







