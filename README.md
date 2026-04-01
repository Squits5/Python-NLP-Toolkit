# Python-NLP-Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

A versatile Python toolkit for natural language processing (NLP), offering essential utilities for text preprocessing, tokenization, stop-word removal, word frequency analysis, and basic sentiment analysis. Designed for ease of use and integration into larger NLP pipelines.

## Features

-   **Text Cleaning:** Functions to remove URLs, mentions, hashtags, punctuation, and numbers.
-   **Tokenization:** Efficient text splitting into words.
-   **Stop-word Removal:** Filter out common words that add little meaning.
-   **Word Frequency:** Identify the most common words in a document.
-   **Sentiment Analysis:** Basic sentiment scoring using VADER lexicon.

## Project Structure

```
Python-NLP-Toolkit/
├── src/
│   └── nlp_utils.py
├── README.md
└── requirements.txt
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Squits5/Python-NLP-Toolkit.git
    cd Python-NLP-Toolkit
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download NLTK data (if not already present):**
    The script will attempt to download necessary NLTK data (`punkt`, `stopwords`, `vader_lexicon`) if they are not found. You can also do it manually in a Python interpreter:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    ```

## Usage

```python
from src.nlp_utils import NLPProcessor

nlp_processor = NLPProcessor()
sample_text = "This is an amazing library for NLP tasks! I love how easy it is to use."

processed_data = nlp_processor.process_document(sample_text)
print(processed_data["sentiment"])
print(processed_data["word_frequency"])
```

## Contributing

Contributions are welcome! Feel free to suggest new features or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
