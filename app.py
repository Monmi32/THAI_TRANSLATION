import streamlit as st
import time
from translator import translate_english_to_thai
import styles

def main():
    """Main function to run the Streamlit app"""
    
    # Set page configuration
    st.set_page_config(
        page_title="Thai Translator",
        page_icon="🇹🇭",
        layout="centered",
        initial_sidebar_state="expanded"
    )

    # Apply custom CSS and fonts
    st.markdown(styles.get_css(), unsafe_allow_html=True)
    st.markdown(styles.get_font_imports(), unsafe_allow_html=True)

    # Header
    st.markdown(styles.get_header_html(), unsafe_allow_html=True)

    # Sidebar with information
    with st.sidebar:
        st.title("About")
        st.markdown(styles.get_sidebar_content())
        
        st.markdown("---")
        st.markdown("Made with ❤️ using Streamlit and Gemini")

    # Main app
    st.markdown("<div class='translation-box'>", unsafe_allow_html=True)
    english_text = st.text_area("Enter English text", height=150, 
                               placeholder="Type your English text here...",
                               key="english_input")

    translate_button = st.button("Translate to Thai", use_container_width=True)

    # Store translation in session state
    if "translation" not in st.session_state:
        st.session_state["translation"] = ""

    if translate_button and english_text:
        with st.spinner("Translating..."):
            # Add a slight delay to show the spinner
            time.sleep(0.5)
            translation = translate_english_to_thai(english_text)
            if translation:
                st.session_state["translation"] = translation

    st.markdown("</div>", unsafe_allow_html=True)

    # Display translation result
    if "translation" in st.session_state and st.session_state["translation"]:
        st.markdown("<div class='translation-box'>", unsafe_allow_html=True)
        st.subheader("Thai Translation")
        st.markdown(f"<p class='thai-text'>{st.session_state['translation']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)



    # Footer
    st.markdown(styles.get_footer_html(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()