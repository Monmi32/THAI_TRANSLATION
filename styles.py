"""
Custom styles for the Thai translation app
"""

# Main CSS for the app
def get_css():
    return """
    <style>
        .main {
            background-color: #f5f7ff;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .translation-box {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .title-container {
            text-align: center;
            margin-bottom: 30px;
        }
        .flag {
            font-size: 2rem;
            margin: 0 10px;
        }
        .stButton button {
            background-color: #FF6B6B;
            color: white;
            font-weight: bold;
            border-radius: 20px;
            padding: 10px 20px;
            border: none;
        }
        .stButton button:hover {
            background-color: #FF5252;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 0.8rem;
            color: #666;
        }
        .thai-text {
            font-family: 'Sarabun', sans-serif;
            font-size: 1.5rem;
        }
    </style>
    """

# Font imports for Thai text
def get_font_imports():
    return """
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap" rel="stylesheet">
    """

# App header HTML
def get_header_html():
    return """
    <div class="title-container">
        <h1>🇺🇸 English to Thai Translator 🇹🇭</h1>
        <p>Powered by Google Gemini AI</p>
    </div>
    """

# Sidebar content HTML
def get_sidebar_content():
    return """
    This website is made for translation of text from English to Thai.
    
    ### Features
    - Fast and accurate translations
    - Support for sentences, paragraphs, and phrases
    - Pronunciation guide
    
    ### How to use
    1. Enter your English text in the input box
    2. Click 'Translate to Thai'
    3. View your translation result
    
    ### About Thai language
    Thai (ภาษาไทย) is the national language of Thailand and is spoken by about 60 million people worldwide.
    """

# Footer HTML
def get_footer_html():
    return """
    <div class="footer">
        <p>© 2025 Thai Translator App | This application uses Google Gemini AI for translations</p>
    </div>
    """

# Example phrases for the app
def get_example_phrases():
    return [
        "Hello, how are you?",
        "My name is John",
        "Where is the nearest restaurant?",
        "Thank you very much",
        "I love Thailand"
    ]