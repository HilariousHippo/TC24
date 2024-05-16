import streamlit as st

# Define your markdown content for each section or chapter
markdown_sections = {
    "Welcome": """
    # Welcome to your Lab Manual!

    ## 🔑 Your Tableau Cloud Credentials

    - Your username is `@lab.CloudCredential(TC24HoT1797).Username`
    - Your password is `@lab.CloudCredential(TC24HoT1797).Password`

    > This credential is assigned to ***only you***. Please don’t share it with anyone else. These credentials are only available during the hands-on training session that you are currently attending.
    """,

    "Let's Get Started": """
    # Let's Get Started!

    ## 💫 Step 1. Access Tableau Cloud

    1. Click the Google Chrome Shortcut on your VM. You will see the Tableau Cloud sign-in page.
    2. Copy & paste your `@lab.CloudCredential(TC24HoT1797).Username` into Tableau Cloud’s sign-in page and click [Sign In].
    3. You will be redirected to Auth0’s sign-in page. Don’t worry, you are at the right place. Type again your `@lab.CloudCredential(TC24HoT1797).Username` and `@lab.CloudCredential(TC24HoT1797).Password`. Click [Continue].
    4. You should now be signed in to Tableau Cloud!
    """,

    "Chapter 1 - Build & Publish": """
    # ✍ Chapter 1: Build & Publish

    ## 💡 Key Points

    - In this chapter, you will create a workbook using the existing published data source.
    - You will experience how to create Tableau’s dashboard.
    - By publishing your workbook to Tableau Cloud, your content will be available to anyone who has the right permissions.

    ## 📚 Resource Links

    - [Getting Started with web authoring](https://help.tableau.com/current/pro/desktop/en-us/getstarted_web_authoring.htm)
    - [Best Practices for Published Data Sources](https://help.tableau.com/current/pro/desktop/en-us/publish_datasources_about.htm)
    """
}

# Render navigation buttons for each section or chapter
current_section = st.sidebar.selectbox("Navigate to", list(markdown_sections.keys()))

# Display the selected section or chapter
st.markdown(markdown_sections[current_section])
