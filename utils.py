import re

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def preprocess_text(self):
        """
        Preprocess the text: remove whitespaces, newlines, and special characters.
        """
        self.text = re.sub(r'<[^>]*?>', '', self.text)  # Remove HTML tags
        self.text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', self.text)  # Remove URLs
        self.text = self.text.strip()
        self.text = re.sub(r'\n+', ' ', self.text)
        self.text = re.sub(r'\s+', ' ', self.text)
        self.text = re.sub(r'[^A-Za-z0-9\s.,!?\'"-]', '', self.text)
        words = self.text.split()
        words = words[:3000]
        self.text = ' '.join(words)
        return self.text
