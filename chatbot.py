import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class FashionChatbot:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

        # Define rules and corresponding responses
        self.rules = {
            'clothes|clothing|apparel': 'Explore our latest collection of trendy and stylish clothing. You will get a variety of clothing like shirts, trousers, tops, hoodies, skirts etc.',
            'shoes': 'Discover our wide range of fashionable shoes for all occasions.', 'hi':'Hello! How can I help you?',
            'accessories': 'Complete your look with our trendy accessories, including jewelry and bags.',
            'new arrivals': 'Check out our new arrivals for the latest fashion trends.',
            'sale|discount': 'Don\'t miss out on our ongoing sale! Get great discounts on selected items.',
            'order status': 'You can check your order status by logging into your account on our website.',
            'contact': 'For any inquiries, please contact our customer support at support@fashionista.com.',
            'good morning': 'Good morning! How can I assist you with your fashion needs today?',
            'good afternoon': 'Good afternoon! How can I help you find in our fashion collection?',
            'good evening': 'Good evening! How may I assist you in choosing the perfect outfit?',
            'bye|goodbye': 'Thank you for visiting Fashionista! Have a stylish day!'
        }

    def preprocess_input(self, user_input):
        # Tokenize, remove stop words, and lemmatize the input
        tokens = word_tokenize(user_input.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in self.stop_words]
        return tokens

    def respond(self, user_input):
        # Preprocess user input
        tokens = self.preprocess_input(user_input)

        # Check user input against rules
        for pattern, response in self.rules.items():
            if any(re.search(keyword, user_input, re.IGNORECASE) for keyword in pattern.split('|')):
                return response

        # If no match, respond with a default message
        return "I'm sorry, I don't understand that."

def main():
    fashion_bot = FashionChatbot()
    print("Fashion Chatbot: Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Fashion Chatbot: Thank you for visiting FASHIONISTA! Stay stylish!")
            break

        response = fashion_bot.respond(user_input)
        print("Fashion Chatbot:", response)

if __name__ == "__main__":
    main()