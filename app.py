import streamlit as st

# Define markdown content for each section
markdown_sections = {
    "Welcome": """
    # Welcome to your Lab Manual!
    "🔑 Your Tableau Cloud Credentials": """
        Your user name is **@lab.CloudCredential(TC24HoT1797).Username**.
        Your password is **@lab.CloudCredential(TC24HoT1797).Password**.
        This credentials are assign to only you. Please do not share this with anyone else.
        """,
    "Let's get it started!": """
        ### 💫 Step 1. Access Tableau Cloud
        Click the Google Chrome Shortcut on your VM. You will see Tableau Cloud sign-in page.
        Copy & paste your `@lab.CloudCredential(TC24HoT1797).Username` into Tableau Cloud{{SINGLE_QUOTE}}s sign-in page and click [Sign In].
        You will be redirected to Auth0{{SINGLE_QUOTE}}s sign-in page. Type again your `@lab.CloudCredential(TC24HoT1797).Username` 
        and `@lab.CloudCredential(TC24HoT1797).Password`. Click [Continue].
        """,
    "✍ Chapter 1: Build & Publish": """
        ### 💡 Key Points
        - In this chapter, you will create a workbook using the existing published data source.
        - You will experience how to create Tableau{{SINGLE_QUOTE}}s dashboard.
        - By publishing your workbook to Tableau Cloud, your content will be available to anyone who has the right permissions.
        """
    # Add more sections here with replaced single quotes
}

# Render the markdown content with a button at the bottom
def render_markdown_with_button(section_content):
    st.markdown(section_content, unsafe_allow_html=True)
    st.write("")  # Add a space for layout
    st.button("Go to Next Section", key=section_content[:20])  # Button to navigate to next section

# Main function to run the app
def main():
    st.sidebar.title("Navigation Bar")
    selected_section = st.sidebar.radio("Go to", list(markdown_sections.keys()))

    st.title(selected_section)
    render_markdown_with_button(markdown_sections[selected_section])

if __name__ == "__main__":
    main()
