"""
Custom styles for the Thai translation app (Dark Mode)
"""

# Main CSS for dark theme
def get_css():
    return """
    <style>
        .main {
            background-color: #121212;
            color: #e0e0e0;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .translation-box {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.6);
            margin-bottom: 20px;
        }
        .title-container {
            text-align: center;
            margin-bottom: 30px;
            color: #ffffff;
        }
        .flag {
            font-size: 2rem;
            margin: 0 10px;
        }
        .stButton button {
            background-color: #bb86fc;
            color: white;
            font-weight: bold;
            border-radius: 20px;
            padding: 10px 20px;
            border: none;
        }
        .stButton button:hover {
            background-color: #985eff;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 0.8rem;
            color: #999;
        }
        .thai-text {
            font-family: 'Sarabun', sans-serif;
            font-size: 1.5rem;
        }
    </style>
    """

def get_font_imports():
    return """
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap" rel="stylesheet">
    """

def get_header_html():
    return """
    <div class="title-container">
        <h1>🇺🇸 English to Thai Translator 🇹🇭</h1>
        <p>Powered by Google Gemini AI with Text-to-Speech</p>
    </div>
    """

def get_sidebar_content():
    return """
    This app uses Google's Gemini AI to translate text from English to Thai.

    ### Features
    - Fast and accurate translations
    - Support for full sentences and paragraphs
    - Text-to-Speech for English and Thai

    ### How to use
    1. Enter your English text
    2. Click 'Translate to Thai'
    3. See and hear your translation

    ### About Thai language
    Thai (ภาษาไทย) is the national language of Thailand and is spoken by over 60 million people worldwide.
    """

def get_footer_html():
    return """
    <div class="footer">
        <p>© 2025 Thai Translator App | Built with Google Gemini AI</p>
    </div>
    """
