import streamlit as st

def main():
    st.title("Welcome to your Lab Manual!")
    
    # Load and render your markdown file
    with open("lab_manual.md", "r", encoding="utf-8") as file:
        markdown_text = file.read()
        st.markdown(markdown_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
