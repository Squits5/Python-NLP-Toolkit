import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure NLTK data is downloaded (run once)
try:
    stopwords.words('english')
    word_tokenize('test')
    SentimentIntensityAnalyzer()
except LookupError:
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('vader_lexicon')

class NLPProcessor:
    def __init__(self, language='english'):
        self.stop_words = set(stopwords.words(language))
        self.sid = SentimentIntensityAnalyzer()

    def clean_text(self, text):
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        # Remove mentions and hashtags
        text = re.sub(r'@\w+|#\w+', '', text)
        # Remove punctuation and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        return text

    def tokenize_text(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        return [word for word in tokens if word not in self.stop_words]

    def get_word_frequency(self, text, num_words=10):
        cleaned_text = self.clean_text(text)
        tokens = self.tokenize_text(cleaned_text)
        filtered_tokens = self.remove_stopwords(tokens)
        return Counter(filtered_tokens).most_common(num_words)

    def analyze_sentiment(self, text):
        # VADER sentiment analysis returns a dictionary of scores
        # for negative, neutral, positive, and compound.
        return self.sid.polarity_scores(text)

    def process_document(self, document):
        cleaned = self.clean_text(document)
        tokens = self.tokenize_text(cleaned)
        filtered_tokens = self.remove_stopwords(tokens)
        sentiment = self.analyze_sentiment(document) # Analyze sentiment on original text for better context
        word_freq = self.get_word_frequency(document)
        
        return {
            "original_text": document,
            "cleaned_text": cleaned,
            "tokens": tokens,
            "filtered_tokens": filtered_tokens,
            "sentiment": sentiment,
            "word_frequency": word_freq
        }

if __name__ == "__main__":
    nlp_processor = NLPProcessor()
    sample_text = (
        "This is an amazing library for NLP tasks! I love how easy it is to use. "
        "It handles text cleaning, tokenization, and even sentiment analysis. "
        "Check out https://example.com for more info. #NLP #Python"
    )

    print("
--- Processing Sample Text ---")
    processed_data = nlp_processor.process_document(sample_text)
    for key, value in processed_data.items():
        print(f"{key}: {value}")

    another_text = "I hate this product. It's terrible and useless."
    print("
--- Processing Another Text (Negative) ---")
    print(nlp_processor.analyze_sentiment(another_text))

    neutral_text = "The quick brown fox jumps over the lazy dog."
    print("
--- Processing Another Text (Neutral) ---")
    print(nlp_processor.analyze_sentiment(neutral_text))
