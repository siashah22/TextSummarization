# TextSummarization

# DESCRIPTION OF THE PROJECT :
This project demonstrates a Python-based text summarization tool using Natural Language Processing (NLP) techniques. The tool accepts lengthy articles or textual content as input and generates a concise summary by identifying and retaining the most relevant sentences.

Libraries Used in the Project:

1.NLTK (Natural Language Toolkit): A comprehensive library for natural language processing tasks.

2.collections.Counter: A Python standard library for counting the occurrences of elements in a collection.Used to compute word frequencies.

3.heapq: A Python standard library for working with heaps (priority queues). Used to efficiently retrieve the highest-scoring sentences for the summary.

Key Features:

1.Tokenization: Breaks the text into sentences and words.

2.Stopword Removal: Removes common, insignificant words (e.g., "and," "the") to focus on meaningful terms.

3.Word Frequency Analysis: Assigns importance to words based on their frequency in the text.

4.Sentence Scoring: Scores sentences based on the cumulative importance of words they contain.

5.Summary Extraction: Selects top-scoring sentences to generate the summary, ensuring brevity while retaining context.

# INPUT

Enter the text to be summarized:


Artificial intelligence (AI) is a set of technologies that empowers computers to learn, reason, and perform a variety of advanced tasks in ways that used to require human intelligence, such as understanding language, analyzing data, and even providing helpful suggestions. It’s a transformational technology that can bring meaningful and positive change to people and societies and the world.It encompasses many different disciplines, including computer science, data analytics and statistics, hardware and software engineering, linguistics, neuroscience, and even philosophy and psychology. AI is about teaching computers to do the amazing things our own brains can do, from understanding the world around them to learning new things and even coming up with fresh ideas. For instance, AI is used in optical character recognition (OCR) to pull text and data from various images and documents. This process transforms unstructured content into structured, business-ready data, helping uncover valuable insights.Artificial intelligence techniques, though diverse, all fundamentally rely on data, algorithms, and computational power. AI systems learn and improve through exposure to vast amounts of data, identifying patterns and relationships that humans might miss. This data serves as the training material, the quality and quantity of which are crucial for the AI's performance.
# OUTPUT

Summarized Text:

This process transforms unstructured content into structured, business-ready data, helping uncover valuable insights.Artificial intelligence techniques, though diverse, all fundamentally rely on data, algorithms, and computational power. AI systems learn and improve through exposure to vast amounts of data, identifying patterns and relationships that humans might miss.


