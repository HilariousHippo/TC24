import streamlit as st

def render_markdown_file(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as file:
        markdown_text = file.read()
        # Render the markdown content using st.markdown
        st.markdown(markdown_text, unsafe_allow_html=True)

def main():
    st.title("Welcome to your Lab Manual!")
    # Path to your markdown file
    markdown_file = "lab_manual.md"
    render_markdown_file(markdown_file)

if __name__ == "__main__":
    main()
