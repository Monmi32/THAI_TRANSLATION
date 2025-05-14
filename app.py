import streamlit as st
from translator import translate_english_to_thai, synthesize_speech
from styles import get_css, get_font_imports, get_header_html, get_sidebar_content, get_footer_html

st.set_page_config(page_title="English to Thai Translator", layout="centered")

# Inject styling
st.markdown(get_font_imports(), unsafe_allow_html=True)
st.markdown(get_css(), unsafe_allow_html=True)

# Header
st.markdown(get_header_html(), unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown(get_sidebar_content())

# Main translation UI
with st.container():
    st.markdown('<div class="translation-box">', unsafe_allow_html=True)
    english_text = st.text_area("Enter English Text", height=150)

    if st.button("Translate to Thai"):
        if english_text.strip():
            thai_text = translate_english_to_thai(english_text)

            if thai_text:
                st.markdown(f'<p class="thai-text">🇹🇭 {thai_text}</p>', unsafe_allow_html=True)

                # English TTS
                eng_audio_path = synthesize_speech(english_text, lang='en')
                if eng_audio_path:
                    st.markdown("🔊 English Pronunciation")
                    st.audio(eng_audio_path, format="audio/mp3", start_time=0)

                # Thai TTS
                thai_audio_path = synthesize_speech(thai_text, lang='th')
                if thai_audio_path:
                    st.markdown("🔊 Thai Pronunciation")
                    st.audio(thai_audio_path, format="audio/mp3", start_time=0)
            else:
                st.error("Translation failed. Please try again.")
        else:
            st.warning("Please enter some English text.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(get_footer_html(), unsafe_allow_html=True)
