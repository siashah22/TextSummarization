#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import heapq

# Download NLTK data files (only need to run this once)
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, summary_ratio=0.2):
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

# Example usage
if __name__ == "__main__":
    input_text = """
    Natural Language Processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between
    computers and humans through natural language. The ultimate objective of NLP is to read, decipher, understand, and
    make sense of human languages in a manner that is valuable. Applications of NLP are seen in translation services,
    sentiment analysis, chatbots, and many other areas. As the field advances, its potential to revolutionize technology
    continues to grow.
    """
    
    print("Original Text:\n", input_text)
    print("\nSummarized Text:\n", summarize_text(input_text))


# In[6]:


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import heapq

# Download NLTK data files (only need to run this once)
# nltk.download('punkt')
# nltk.download('stopwords')

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


# In[ ]:




